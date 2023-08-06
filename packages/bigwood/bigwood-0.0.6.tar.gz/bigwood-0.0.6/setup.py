from pathlib import Path
from setuptools import setup, find_packages

# apparently I need this

# The text of the README file
readme = Path(Path(__file__).parent, "README.md").read_text()

# call setup to do the shiz
setup(
    name="bigwood",
    version="0.0.6",
    description="Packaged utility tools for bigwood",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="christopherhwoodall@gmail.com",
    license="MIT",
    packages=['bigwood'],
    include_package_data=True,
)
