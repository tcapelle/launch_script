from setuptools import setup

exec(open("src/wandbize/version.py").read())

setup(
    version=__version__,
)
