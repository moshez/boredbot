import os
import shutil
import subprocess

import pex

def buildWheels():
    shutil.rmtree('build/wheelhouse')
    subprocess.check_call(['pip', 'wheel', '--requirement', 'requirements.txt', '--wheel-dir', 'build/wheelhouse'])
    subprocess.check_call(['pip', 'wheel', 'setuptools==15.2', '--wheel-dir', 'build/wheelhouse'])
    subprocess.check_call(['pip', 'wheel', '.', '--wheel-dir', 'build/wheelhouse'])

def buildPEX():
    if os.path.exists('build/boredbot.pex'):
        os.remove('build/boredbot.pex')
    subprocess.check_call(['pex', '--repo', 'build/wheelhouse', '--no-index', '--output-file', 'build/boredbot.pex',
                           '--disable-cache', '--requirement', 'requirements.txt', 'boredbot', '--entry-point', 'boredbot'])

BOREDBOT_MAIN_OK = True
def main(dummyArgs):
    buildWheels()
    buildPEX()
