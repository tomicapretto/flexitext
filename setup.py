import codecs
import os
import sys

from setuptools import find_packages, setup

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
README_FILE = os.path.join(PROJECT_ROOT, "README.md")
VERSION_FILE = os.path.join(PROJECT_ROOT, "flexitext", "version.py")
REQUIREMENTS_FILE = os.path.join(PROJECT_ROOT, "requirements.txt")



def get_long_description():
    with codecs.open(README_FILE, "rt") as buff:
        return buff.read()


def get_requirements():
    with codecs.open(REQUIREMENTS_FILE) as buff:
        return buff.read().splitlines()


version_info = {}
with open(VERSION_FILE) as version_file:
    exec(version_file.read(), version_info)


setup(
    name="flexitext",
    version=version_file["__version__"],
    author=version_info["__author__"],
    author_email=version_info["__author_email__"],
    url="https://github.com/tomicapretto/flexitext",
    description="Add custom text to Matplotlib plots in a flexible way",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    install_requires=get_requirements(),
    maintainer=version_file["__author__"],
    maintainer_email=version_file["__author_email__"],
    packages=find_packages(),
    license="MIT",
     python_requires=">=3.6",
)