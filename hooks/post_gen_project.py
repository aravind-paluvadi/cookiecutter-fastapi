"""Scripts run in the root directory of the generated project."""
#!/usr/bin/env python
# Standard Library Imports
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str):
    """Remove a file."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")

    if "{{ cookiecutter.create_manifest_file }}" != "y":
        remove_file("MANIFEST.in")
