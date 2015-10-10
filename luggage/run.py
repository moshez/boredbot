import os
import shutil
import sys

from ncolony import ctllib

def calcCommandline():
    """return a command-line prefix that will run me

    :rettype: list of strings
    """
    argv0 = sys.argv[0]
    if not argv0.endswith('__main__.py'):
        return [argv0]
    prefix = os.path.dirname(argv0)
    path = map(os.path.abspath, sys.path)
    while prefix not in path:
        up = os.path.dirname(prefix)
        if up == prefix:
            raise RuntimeError('Could not find prefix', argv0)
        prefix = up
    module = '.'.join(argv0[len(prefix):].split('/')[1:-1])
    return [sys.executable, '-m', module]

def mkconfig(dirname):
    """create an NColony configuration

    :param dirname: directory in which to create the configuration
    :type dirname: string
    :rettype: ncolony.ctllib.Places
    """
    place = os.path.abspath(dirname)
    if os.path.exists(place):
        shutil.rmtree(place)
    os.mkdir(place)
    config = os.path.join(place, 'config')
    messages = os.path.join(place, 'messages')
    places = ctllib.Places(config=config, messages=messages)
    for dr in places:
        os.mkdir(dr)
    return places
