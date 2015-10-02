import pex

def buildWheels():
    subprocess.check_call(['pip', 'wheel', '--requirement', 'requirements.txt', '--wheel-dir', 'build/wheelhouse'])
    subprocess.check_call(['pip', 'wheel', '.', '--wheel-dir', 'build/wheelhouse'])

BOREDBOT_MAIN_OK = True
def main():
    buildWheels()
