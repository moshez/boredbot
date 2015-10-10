import os
import sys

from twisted.scripts import twistd

from ncolony import ctllib

from luggage import run

BOREDBOT_MAIN_OK = True
def main(args):
    cmdLine = run.calcCommandline()
    places = run.mkconfig('boredbot-config')
    ctllib.add(places, 'boredbot', cmd=cmdLine[0], args=cmdLine[1:] + ['loop'],
               env=['SECRET_KEY='+os.environ['SECRET_KEY']])
    ctllib.add(places, 'boredweb', cmd=cmdLine[0], args=cmdLine[1:] + ['gunicorn', '-w', '4', 'boredbot_deploy.wsgi:app'],
               env=['SECRET_KEY='+os.environ['SECRET_KEY']])
    sys.argv = ['twistd', '--nodaemon', 'ncolony', '--messages', places.messages, '--config', places.config]
    twistd.run()