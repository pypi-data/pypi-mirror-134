from distutils.core import setup
from setuptools import find_packages
import os

# Optional project description in README.md:
current_directory = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''
setup(

# Project name: 
name='not_wordle',

# Packages to include in the distribution: 
packages=find_packages(','),

# Project version number:
version='0.0.2',

# List a license for the project, eg. MIT License
license='OSI Approved :: MIT License',

# Short description of your library: 
description='Definitely Not Wordle',

# Long description of your library: 
long_description=long_description,
long_description_content_type='text/markdown',

# Your name: 
author='Mark',

# Your email address:
author_email='mark@sharebite.com',

# Link to your github repository or website: 
url='https://github.com/mark-shbt/definitely-not-wordle',

# Download Link from where the project can be downloaded from:
download_url='https://github.com/mark-shbt/definitely-not-wordle',

# List of keywords: 
keywords=[],

# List project dependencies: 
install_requires=[
'certifi',
'charset-normalizer',
'idna',
'nose',
'PyYAML',
'Random-Word',
'requests',
'urllib3',
],

# https://pypi.org/classifiers/ 
classifiers=[]
)