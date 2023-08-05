[tox]
envlist =
    py27,

[testenv]
basepython =
    py27: python2.7

commands =
    pip install machinepack
    pymachine test