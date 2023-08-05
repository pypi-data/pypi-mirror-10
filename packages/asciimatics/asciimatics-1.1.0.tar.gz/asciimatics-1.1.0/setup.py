"""
A setuptools based setup module for asciimatics.

Based on the sample Python packages at:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='asciimatics',
    version='1.1.0',
    description='An ASCII art and text cinematic storyboard/demo library',
    long_description=long_description,
    url='https://github.com/peterbrittain/asciimatics.git',
    author='Peter Brittain',
    author_email='',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: General',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    keywords='ascii art demo credits title sequence',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'pyfiglet >= 0.7.2',
        'Pillow >= 2.7.0',
    ],
)
