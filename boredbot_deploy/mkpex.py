from luggage import buildpex

BOREDBOT_MAIN_OK = True
def main(dummyArgs):
    wheelhouse = buildpex.buildWheels('build', 'requirements.txt')
    buildpex.buildPEX(wheelhouse, 'build/boredbot.pex', 'requirements.txt', 'boredbot_deploy', ['boredbot'])
