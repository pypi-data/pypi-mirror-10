${'# -*- coding: utf-8 -*-'}

CONFIG = {
    'name': "machinepack_${machinepack_name}",
    'version': "${version}",
    'author': "${author}",
    'author_email': "${author_email}",
    'description': "${machinepack_description}",
    'license': "MIT",
    'keywords': "${keywords}",
    'url': "http://packages.python.org/machinepack_${machinepack_name}",
    'packages': ["machinepack_${machinepack_name}"],
    'classifiers': [
    % for c in context['classifiers']:
       "${c}",
    % endfor
    ],
    'install_requires': [
        'machinepack'
    ],

    # Machinepack global config specification
    'machinepack_config': {
    }
}