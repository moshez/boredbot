import flask
import requests

blueprint = flask.Blueprint('showbored', __name__)

@blueprint.route('/')
def showEntries():
    headers = flask.current_app.config['headers']
    stateHeaders = flask.current_app.config['stateHeaders']
    lines  = requests.get('https://api.parse.com/1/classes/lines', headers=headers).json()['results']
    status, = requests.get('https://api.parse.com/1/classes/current', headers=stateHeaders).json()['results']
    output = ['<html><body>%s<ul>' % status['feeling']]
    for line in lines:
        output.append('<li>%(status)s (%(updatedAt)s)</li>' % line)
    output.append('</ul></body><html>')
    return '\n'.join(output)
