from pathlib import Path

import toml

PYPROJECT_PATH = Path(__file__).parent.parent / 'pyproject.toml'

def parse_version_from_pyproject_file(pyproject_file: Path) -> str:
    """
    Parse the version from a pyproject.toml file.
    """
    with open(pyproject_file) as f:
        pyproject_data = toml.load(f)
    return pyproject_data['tool']['poetry']['version']


__version__ = parse_version_from_pyproject_file(PYPROJECT_PATH)
