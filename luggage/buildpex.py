import os
import shutil
import subprocess

import pex

def buildWheels(buildDir, requirements):
    """build wheels

    :param buildDir: directory to put wheels in (under 'wheelhouse')
    :type buildDir: string
    :param requirements: name of file holding names of Python packages
    :type requirements: string
    """
    wheelhouse = os.path.join(buildDir, 'wheelhouse')
    if os.path.exists(wheelhouse):
        shutil.rmtree(wheelhouse)
    subprocess.check_call(['pip', 'wheel', '--requirement', requirements, '--wheel-dir', wheelhouse])
    subprocess.check_call(['pip', 'wheel', 'setuptools==15.2', '--wheel-dir', wheelhouse])
    subprocess.check_call(['pip', 'wheel', '.', '--wheel-dir', wheelhouse])
    return wheelhouse

def buildPEX(wheelhouse, output, requirements, module, localwheels):
    """build pex file

    :param wheelhouse: path to directory containing wheel
    :type wheelhouse: string
    :param requirements: name of file holding names of Python packages
    :type requirements: string
    :param module: module to run 'python -m' on in Pex
    :type module: string
    :param localwheels: wheels to build locally
    :type localwheels: list of strings
    """
    if os.path.exists(output):
        os.remove(output)
    subprocess.check_call(['pex', '-o', output])
    subprocess.check_call(['pex', '--repo', wheelhouse, '--no-index', '--output-file', output,
                           '--disable-cache',
                           '--requirement', requirements, '--entry-point', module] + localwheels)
