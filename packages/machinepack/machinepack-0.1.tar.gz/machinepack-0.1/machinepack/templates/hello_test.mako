from machinepack.pack import MockResult
from machinepack.pack import MachineResponse

tests = [
    {
      'description': "Sample hello test",
      'inputs': {'name': 'John'},
      'exit': MachineResponse('success', welcome_msg='Hello John!'),
    }
]