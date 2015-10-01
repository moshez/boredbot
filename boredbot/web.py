import flask

app = flask.Flask('bored-web')

BOREDBOT_MAIN_OK = True

def main(dummyArgs):
    app.run()
