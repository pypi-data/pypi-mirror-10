${'# -*- coding: utf-8 -*-'}

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