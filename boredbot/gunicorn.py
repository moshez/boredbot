from __future__ import absolute_import

from gunicorn.app import base as gabase

from boredbot import web

BOREDBOT_MAIN_OK = True

class NoLoadApplication(gabase.BaseApplication):
    def load_config(self):
        pass

def main(args):
    gapp = NoLoadApplication()
    gapp.callable = web.app
    gapp.run()
