## Build a Pex from the requirements and the local 'boredbot' wheel
## Behave as though it's running 'python -m boredbot_deploy'
from luggage import buildpex

BOREDBOT_MAIN_OK = True
def main(dummyArgs):
    wheelhouse = buildpex.buildWheels('build', 'requirements.txt')
    buildpex.buildPEX(wheelhouse, 'build/boredbot.pex', 'requirements.txt', 'boredbot_deploy', ['boredbot'])
