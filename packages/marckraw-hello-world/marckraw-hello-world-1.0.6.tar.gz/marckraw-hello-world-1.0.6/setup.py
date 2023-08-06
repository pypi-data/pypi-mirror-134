import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="marckraw-hello-world",
    version="1.0.6",
    packages=["marckraw-hello-world"], # find_package() - search for packages that are available
    description="Sample PYPI App",
    long_description=README,
    long_description_content_type="text/markdown",
)
