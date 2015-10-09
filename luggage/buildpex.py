import os
import shutil
import subprocess

import pex

def buildWheels(buildDir, requirements):
    wheelhouse = os.path.join(buildDir, 'wheelhouse')
    if os.path.exists(wheelhouse):
        shutil.rmtree(wheelhouse)
    subprocess.check_call(['pip', 'wheel', '--requirement', requirements, '--wheel-dir', wheelhouse])
    subprocess.check_call(['pip', 'wheel', 'setuptools==15.2', '--wheel-dir', wheelhouse])
    subprocess.check_call(['pip', 'wheel', '.', '--wheel-dir', wheelhouse])
    return wheelhouse

def buildPEX(wheelhouse, output, requirements, module, localwheels):
    if os.path.exists(output):
        os.remove(output)
    subprocess.check_call(['pex', '-o', output])
    subprocess.check_call(['pex', '--repo', wheelhouse, '--no-index', '--output-file', output,
                           '--disable-cache',
                           '--requirement', requirements, '--entry-point', module] + localwheels)
