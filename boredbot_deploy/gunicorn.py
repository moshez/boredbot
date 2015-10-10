## Since we will only have one command-line
## available (equivalent to python -m boredbot_deploy)
## we proxy the gunicorn entry point here.
from __future__ import absolute_import
import sys

from gunicorn.app import wsgiapp

BOREDBOT_MAIN_OK = True
def main(args):
    sys.argv = args
    wsgiapp.run()
