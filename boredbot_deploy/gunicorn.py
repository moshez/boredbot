from __future__ import absolute_import
import sys

from gunicorn.app import wsgiapp

BOREDBOT_MAIN_OK = True
def main(args):
    sys.argv = args
    wsgiapp.run()
