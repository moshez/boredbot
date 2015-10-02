import flask
import requests

from boredbot import config

app = flask.Flask('bored-web')

@app.route('/')
def showEntries():
    lines  = requests.get('https://api.parse.com/1/classes/lines', headers=config.getHeaders()).json()['results']
    status, = requests.get('https://api.parse.com/1/classes/current', headers=config.getStateHeaders()).json()['results']
    output = ['<html><body>%s<ul>' % status['feeling']]
    for line in lines:
        output.append('<li>%(status)s (%(updatedAt)s)</li>' % line)
    output.append('</ul></body><html>')
    return '\n'.join(output)

BOREDBOT_MAIN_OK = True
def main(dummyArgs):
    app.run(debug=True, use_debugger=False, use_reloader=False)
