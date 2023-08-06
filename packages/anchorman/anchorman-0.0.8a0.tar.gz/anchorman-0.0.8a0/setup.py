#!/usr/bin/env python
import anchorman

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from codecs import open
with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='anchorman',
    version=anchorman.__version__,
    description='Markup terms in text',
    long_description=readme,
    author='Tarn Barford, Matthias Rebel',
    author_email='matthias.rebel@gmail.com',
    url='https://github.com/rebeling/anchorman.git',
    license='Apache 2.0',
    packages=['anchorman'],
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'anchorman': 'anchorman'},
    include_package_data=True,
    install_requires=['lxml', 'regex'],
    tests_require=['pytest', 'pytest-cov']
)
