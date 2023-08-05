import os
from setuptools import setup


setup(
    name = "deflake",
    version = "0.0.5",
    author = "NCBI",
    author_email = "",
    description = ("A program to debug flakey programs"),
    license = "Public Domain",
    keywords = "testing flaky",
    url = "http://packages.python.org/deflake",
    entry_points = {
        'console_scripts': 
            ['deflake=deflake.cli:main']
    },
    packages = ["deflake"]
)
