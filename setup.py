from setuptools import setup

setup(
    name='PythonHackerRank',
    version='0.1dev',
    package_dir={"":"src"},
    packages=['hackerrank',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('readme.md').read(),
)