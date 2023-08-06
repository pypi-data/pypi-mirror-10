# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import os

__all__ = ["pid_is_running", "write_pidfile_or_die",
    "ProcessAlreadyRunning"]

def pid_is_running(pid):
    """
    Return pid if pid is still going.

    >>> import os
    >>> mypid = os.getpid()
    >>> mypid == pid_is_running(mypid)
    True
    >>> pid_is_running(1000000) is None
    True
    """

    try:
        os.kill(pid, 0)

    except OSError:
        return

    else:
        return pid

def write_pidfile_or_die(path_to_pidfile):

    if os.path.exists(path_to_pidfile):
        pid = int(open(path_to_pidfile).read())

        if pid_is_running(pid):
            msg = "Sorry, found a pidfile!  Process {0} is still running.".format(pid)
            raise ProcessAlreadyRunning(msg)

        else:
            os.remove(path_to_pidfile)

    open(path_to_pidfile, 'w').write(str(os.getpid()))
    return path_to_pidfile


class ProcessAlreadyRunning(Exception):
    pass
