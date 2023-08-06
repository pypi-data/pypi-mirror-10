"""
Lancet consists of three fundamental class types: Argument Specifiers,
Command Templates and Launchers. The review_and_launch decorator is a
helper utility that helps coordinate the use of these objects.

Argument Specifiers
-------------------

Argument specifiers are intended to offer a succinct, declarative and
composable way of specifying large parameter sets. High-dimensional
parameter sets are typical of large-scale scientific models and can
make specifying such models and simulations difficult. Using argument
specifiers, you can document how the parameters of your model vary
across runs without extended lists of arguments or requiring deeply
nested loops.

Argument specifiers can be freely intermixed with Python code,
simplifying the use of scientific software with a Python
interface. They also invoke commandline programs using CommandTemplate
objects to build commands and Launcher objects to execute
them. Argument specifiers can compose together using Cartesian
Products or Concatenation to express huge numbers of argument sets
concisely. In this way they can help simplify the management of
simulation, analysis and visualisation tools with Python.

Command Templates
------------------

When working with external tools, a command template is needed to turn
an argument specifier into an executable command. These objects are
designed to be customisable with sensible defaults to reduce
boilerplate. They may require argument specifiers with a certain
structure (certain argument names and value types) to operate
correctly.

Launchers
---------

A Launcher is designed to execute commands on a given computational
platform, making use of as much concurrency where possible. The
default Launcher class executes commands locally while the QLauncher
class is designed to launch commands on Sun Grid Engine clusters.

The review_and_launch decorator
-------------------------------

This decorator helps codify a pattern of Lancet use that checks for
consistency and offers an in-depth review of all settings before
launch. The goal is to help users identify mistakes early before
consuming computational time and resources.
"""

import os, sys, subprocess
import param

__version__ = param.Version(release=(0,9,0), fpath=__file__, commit="$Format:%h$")

from lancet.core import *       # pyflakes:ignore (appropriate import)
from lancet.dynamic import *    # pyflakes:ignore (appropriate import)
from lancet.launch import *     # pyflakes:ignore (appropriate import)
from lancet.filetypes import *  # pyflakes:ignore (appropriate import)


class vcs_metadata(param.ParameterizedFunction):
    """
    Simple utility to capture basic version control information for
    Git, SVN and Mercurial. Returns a dictionary with the version,
    latest commit message and the diffs relative to the current
    working directories. Can be customized by setting the commands
    dictionary at the class level.
    """
    paths = param.List(default=[], doc="""
       List of repositories to generate version control information from.""")

    commands = param.Dict(default={'.git':(['git', 'rev-parse', 'HEAD'],
                                           ['git', 'log', '--oneline', '-n', '1'],
                                           ['git', 'diff']),
                                   '.svn':(['svnversion'],
                                           ['svn', 'log', '-l', '1', '-q'],
                                           ['svn', 'diff']),
                                   '.hg': (['hg', 'parents', '--template', '"{rev}:{node}"'],
                                           ['hg', 'log',  '-l', '1'],
                                           ['hg', 'diff'])},

       doc="""The subprocess command lists to get the version, commit
       message and diffs for different version control systems. The
       commands are executed if a subdirectory matching the dictionary
       key exists""")

    def __call__(self, paths=[], **params_to_override):
        """
        Takes a single path string or a list of path strings and
        returns the corresponing version control information.
        """
        p=param.ParamOverrides(self, dict(params_to_override, paths=paths))
        if p.paths == []:
            raise Exception("No paths to version controlled repositories given.")

        paths = [p.paths] if isinstance(p.paths, str) else p.paths

        def _desc(path, ind):
            for vcs in p.commands.keys():
                if os.path.exists(os.path.join(path, vcs)):
                    proc = subprocess.Popen(p.commands[vcs][ind],
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, cwd=path)
                    return str(proc.communicate()[0].decode()).strip()

        abspaths = [os.path.abspath(path) for path in paths]
        return {'vcs_versions' : dict((path, _desc(path,0)) for path in abspaths),
                'vcs_messages':  dict((path, _desc(path,1)) for path in abspaths),
                'vcs_diffs':     dict((path, _desc(path,2)) for path in abspaths)}



def repr_pretty_annotated(obj, p, cycle):
    p.text(obj._pprint(cycle, annotate=True))

def repr_pretty_unannotated(obj, p, cycle):
    p.text(obj._pprint(cycle, annotate=False))


_loaded = False

def load_ipython_extension(ip):
    """

    IPython pretty printing support (optional). To load the extension
    you may execute the following in IPython:

    %load_ext lancet
    """
    global _loaded
    if not _loaded:
        _loaded = True
        from lancet import launch
        if sys.version_info[0] == 2:
            launch.input = lambda *args, **kwargs: raw_input(*args, **kwargs)

        plaintext_formatter = ip.display_formatter.formatters['text/plain']
        plaintext_formatter.for_type(Args, repr_pretty_annotated)
        plaintext_formatter.for_type(Command, repr_pretty_unannotated)
        plaintext_formatter.for_type(Launcher, repr_pretty_unannotated)
        plaintext_formatter.for_type(FileType, repr_pretty_unannotated)
        plaintext_formatter.for_type(review_and_launch, repr_pretty_unannotated)
