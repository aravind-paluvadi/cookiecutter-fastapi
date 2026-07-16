"""Scripts run in the root directory of a copy of the repository directory."""
#!/usr/bin/env python
# Standard Library Imports
import sys
import subprocess


def is_docker_installed() -> bool:
    """Check if docker is installed."""
    try:
        subprocess.run(["docker", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    if not is_docker_installed():
        print("Docker is not installed.")
        # sys.exit(1)
