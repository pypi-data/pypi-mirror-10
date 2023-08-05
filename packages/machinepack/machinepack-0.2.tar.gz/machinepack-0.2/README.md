# machinepack

[![Build Status](https://travis-ci.org/python-machine/machinepack.svg?branch=devel)](https://travis-ci.org/python-machine/machinepack)
[![Coverage Status](https://coveralls.io/repos/python-machine/machinepack/badge.svg?branch=devel)](https://coveralls.io/r/python-machine/machinepack?branch=devel)

Installing "machinepack":
```
% python setup.py install
```

## Using `pymachine`:
```
% pymachine
```
```
   ______
  /      \      machinepack (CLI Tool)
 /  |  |  \     v0.1
 \        /
  \______/      http://python-machine.org

Usage: pymachine [OPTIONS] COMMAND [ARGS]...

Options:
  -c, --config PATH
  -v, --version
  -d, --debug
  --help             Show this message and exit.

Commands:
  add      add machine
  browse   view on python-machine.org
  check    get pack metadata
  cp       copy machine
  create   create new machinepack
  example  machine usage example
  exec     run machine
  info     get pack metadata
  ls       list machines
  mv       rename machine
  publish  get pack metadata
  rm       delete existing machine
  source   print machine source
  test     run machine tests
  update   get pack metadata
```

### pymachine create

```
% pymachine create test
```
```
Create successful!
```
Remember to change folder!
```
% cd machinepack_test
```

### pymachine info
```
% pymachine info
```
```
machinepack_test -- No description


URLS
   http://packages.python.org/machinepack_test


INSTALLATION
   pip install machinepack_test


USAGE
   from machinepack_test import Test


AVAILABLE METHODS
    • Test.hello()
```

### pymachine ls

```
% pymachine ls
```
```
There are 1 machines in this machinepack:
=========================================
    ○ Test.hello()
```

### pymachine example 

```
% pymachine example --name hello
```
```python

# -*- coding: utf-8 -*-
from machinepack_test import Test

# Log a hello message with a generated secret code and other information
result = Test.hello(name='John')

# Process result
if result.success:
    print result.success
    # {'welcome_msg': 'Hello John!'}

if result.error:
    print result.error
    # {'description': 'Some error description!'}
```

### pymachine source

```
% pymachine source --name hello
```
```python

# -*- coding: utf-8 -*-

# Metadata goes here
meta = {
    'friendly_name': 'Say hello',
    'description': 'Log a hello message with a generated secret code and other information',
    'extended_description': 'This example machine is part of machinepack-boilerplate, used to introduce everyone to machines.',
    'inputs': {
        'name': {
            'example': 'John',
            'description': 'The name of the person that will be sent the hello message.',
            'required': True
        },
    },
    'default_exit': 'success',
    'exits': {
        'success': {
            'description': 'Success!',
                'example': {
                    'welcome_msg': 'Hello John!'
            },
        },
        'error': {
            'description': 'In case of error',
                'example': {
                    'description': 'Some error description!',
                },
        }
    },
}

# Implementation
def func(inputs, exit, global_conf):

    return exit(
        'success',
        welcome_msg="Hello %s!" % inputs['name']
    )
```

### pymachine exec

```
% pymachine exec --name hello
```
```

Value of 'name': John
Response:
    success

Response params:
    {'welcome_msg': u'Hello John!'}
```

### pymachine test
```
% pymachine test --name hello
```
```

Testing: hello
--------------------
    ⚬ Sample hello test... ✔

Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
machinepack_test/hello       4      0   100%
```

