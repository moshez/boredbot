import os
import shutil
import sys

from twisted.scripts import twistd

from ncolony import ctllib

def calcCommandline():
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

BOREDBOT_MAIN_OK = True
def main(args):
    place = os.path.abspath('boredbot-config')
    if os.path.exists(place):
        shutil.rmtree(place)
    os.mkdir(place)
    config = os.path.join(place, 'config')
    messages = os.path.join(place, 'messages')
    places = ctllib.Places(config=config, messages=messages)
    for dr in places:
        os.mkdir(dr)
    cmdLine = calcCommandline()
    ctllib.add(places, 'boredbot', cmd=cmdLine[0], args=cmdLine[1:] + ['loop'], env=['PARSE_REST_API_KEY='+os.environ['PARSE_REST_API_KEY']])
    ctllib.add(places, 'boredweb', cmd=cmdLine[0], args=cmdLine[1:] + ['web'], env=['PARSE_REST_API_KEY='+os.environ['PARSE_REST_API_KEY']])
    sys.argv = ['twistd', '--nodaemon', 'ncolony', '--messages', messages, '--config', config]
    twistd.run()
