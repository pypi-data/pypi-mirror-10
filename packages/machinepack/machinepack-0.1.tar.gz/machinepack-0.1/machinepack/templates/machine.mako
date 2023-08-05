${'# -*- coding: utf-8 -*-'}

# Metadata goes here
meta = {
    'friendly_name': '',
'description': '',
'extended_description': '',
    'inputs': {
        'name': {
            'example': '',
            'description': '',
            'required': True
        },
    },
    'default_exit': 'success',
    'exits': {
        'success': {
            'description': '',
                'example': {
                    '': ''
            },
        },
        'error': {
            'description': '',
                'example': {
                    '': '',
                },
        }
    },
}

# Implementation
def func(inputs, exit, global_conf):
    return exit('success')