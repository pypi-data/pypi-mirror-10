import os
from setuptools import setup
from machinepack_config import CONFIG

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(**CONFIG)