from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'MAC Generator'
LONG_DESCRIPTION = 'Generates Random Macs'

# Setting up
setup(
    name="jymac",
    version=VERSION,
    author="J0x494949",
    author_email="j0x494949@mej.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'jmax', 'j0x494949', 'jmaxojan', 'hotkeys', 'shortcuts'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True,
    package_data={'': ['*.txt']},
)