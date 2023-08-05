language: python
sudo: false
env:
    - TOXENV=py27
install:
    - travis_retry pip install tox
    - pip install coveralls
    - pip install pylint
script:
    - travis_retry tox
notifications:
email:
    - build-checkins@python-machine.org
after_success:
    - coveralls
