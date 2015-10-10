## WSGI configuration for web UI --
## use the blueprint, and add the
## configuration headers.
import flask

from boredbot import web, parse
from boredbot_deploy import config

app = flask.Flask(__name__)
app.config['headers'] = parse.getHeaders(config.PARSE_APPLICATION_ID, config.SECRETS.get()['PARSE_REST_API_KEY'])
app.config['stateHeaders'] = parse.getHeaders(config.STATE_APPLICATION_ID, config.SECRETS.get()['STATE_REST_API_KEY'])
app.register_blueprint(web.blueprint)
