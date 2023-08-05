${'# -*- coding: utf-8 -*-'}
from ${machinepack_name} import ${machinepack_class}

# ${machinepack_description}
result = ${machinepack_class}.${machine_name}(${", ".join(["%s='%s'" % (input, inputs[input]['example']) for input in inputs])})

# Process result
% for exit in exits:
if result.${exit}:
##    """
##    Result desc: "${exits[exit]['description']}"
##
##    % for param in exits[exit]['example']:
##    ${param} -- (example: "${exits[exit]['example'][param]}", type: "${type(exits[exit]['example'][param]).__name__}")
##    % endfor
##    """
##    % for param in exits[exit]['example']:
##    result.${exit}['${param}']
##    % endfor
    print result.${exit}
    # ${exits[exit]['example']}

% endfor