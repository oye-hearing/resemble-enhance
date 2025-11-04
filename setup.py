from pathlib import Path

from setuptools import setup


def get_inference_requirements(filename: str = 'requirements.inference.txt') -> list[str]:
    """Reads dependencies from the specified requirements file."""
    here = Path(__file__).parent.resolve()
    requirements_path = here / filename

    # Read the file and strip comments/blank lines
    with open(requirements_path, encoding = 'utf-8') as f:
        # Filter out comments and blank lines
        dependencies = [
            line.strip()
            for line in f
            if line.strip() and not line.startswith(('#', '-e', '--'))
        ]
    return dependencies


setup(install_requires = get_inference_requirements(), include_package_data = True)
