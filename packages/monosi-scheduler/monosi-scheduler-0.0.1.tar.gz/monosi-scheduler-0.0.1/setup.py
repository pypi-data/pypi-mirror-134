import pkg_resources
import sys
from os import path
from setuptools import setup, find_packages

if sys.version_info < (3, 0):
    raise Exception("Python 3 or a more recent version is required.")

VERSION = '0.0.1'

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

install_requires = []
with open(path.abspath("requirements.txt"), "r") as f:
    requirements_txt = f.readlines()
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name = 'monosi-scheduler',
    version = VERSION,
    description = 'Monosi Scheduler module',
    long_description=readme,
	author = 'Vocable Inc',
    license=license,
    install_requires=install_requires,
    packages=find_packages(exclude=('tests', 'docs')),
)
