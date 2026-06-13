"""Scripts run in the root directory of the generated project."""
#!/usr/bin/env python
# Standard Library Imports
import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{ cookiecutter.project_slug }}'


# Check if the module name is a valid Python module name
if not re.match(MODULE_REGEX, module_name):
    print(f'ERROR: {module_name} is not a valid Python module name!')

    # Exit to cancel project
    sys.exit(1)
