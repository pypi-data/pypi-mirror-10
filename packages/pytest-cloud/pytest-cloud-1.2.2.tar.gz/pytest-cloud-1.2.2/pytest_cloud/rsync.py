"""Faster rsync."""
import os
import tempfile
import fnmatch
import subprocess

from distutils.spawn import find_executable
import py


def make_reltoroot(roots, args):
    """Non validating make_reltoroot."""
    splitcode = "::"
    l = []
    for arg in args:
        arg = str(arg)
        parts = arg.split(splitcode)
        fspath = py.path.local(parts[0])
        for root in roots:
            x = fspath.relto(root)
            if x or fspath == root:
                parts[0] = root.basename + "/" + x
                break
        l.append(splitcode.join(parts))
    return l


class RSync(object):

    """Send a directory structure (recursively) to one or multiple remote filesystems."""

    def __init__(self, sourcedir, targetdir, verbose=True, ignores=None, includes=None, **kwargs):
        self.sourcedir = str(sourcedir)
        self.targetdir = str(targetdir)
        self.verbose = verbose
        self.ignores = ignores or []
        self.includes = set(includes or [])
        self.targets = set()

    def get_ignores(self):
        """Get ignores."""
        return [str(py.path.local(ignore).relto(os.path.abspath('.'))) for ignore in self.ignores]

    def get_includes(self):
        """Get includes."""
        return [str(py.path.local(include).relto(os.path.abspath('.'))) for include in self.includes]

    def send(self, raises=True):
        """Send a sourcedir to all added targets.

        Flag indicates whether to raise an error or return in case of lack of targets.
        """
        parallel = find_executable('parallel')
        if not parallel:
            raise RuntimeError('parallel is not found.')
        fd_ignores, ignores_path = tempfile.mkstemp()
        fd_includes, includes_path = tempfile.mkstemp()
        fd_ignores = os.fdopen(fd_ignores, 'w')
        fd_includes = os.fdopen(fd_includes, 'w')
        try:
            fd_ignores.writelines(ignore + '\n' for ignore in self.get_ignores())
            fd_ignores.flush()
            fd_includes.writelines(include + '\n' for include in self.get_includes())
            fd_includes.flush()
            subprocess.call([
                parallel, '--verbose', '--gnu', '-j {jobs}',
                'rsync -arHAXvx --ignore-errors --include-from={includes} --exclude-from={ignores} '
                '--numeric-ids --force '
                '--delete-excluded --delete -e \"ssh -T -c arcfour -o Compression=no -o -x\" '
                '. {{}}:{chdir}'.format(
                    chdir=self.targetdir,
                    ignores=ignores_path,
                    includes=includes_path,
                    jobs=len(self.targets),
                ), ':::'
            ] + list(self.targets))
        finally:
            fd_ignores.close()
            fd_includes.close()
            os.unlink(ignores_path)
            os.unlink(includes_path)

    def add_target_host(self, host):
        """Add a remote target."""
        self.targets.add(host)
