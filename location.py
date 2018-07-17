import json
import os
import pip
import pkg_resources
import sys


import yaml


result = {'Python version': sys.version,
          'Virtual environment': os.getenv('PYENV_VERSION'),
          'Python executable location': sys.executable,
          'pip location': pip.__file__,
          'PYTHONPATH': sys.path,
          'Installed packages': [],
          }

for package in pkg_resources.working_set:
    result['Installed packages'].append(str(package))

for i in sys.path:
    if 'site-packages' in i:
        result['Site-packages location'] = i

for element in result:
    print(element, ':', result[element])

with open('output_06.json', 'w') as j_file:
    json.dump(result, j_file)

with open('output_06.yml', 'w') as y_file:
    yaml.dump(result, y_file)
