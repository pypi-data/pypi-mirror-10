#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

if sys.hexversion < 0x03000000: # uniform unicode handling for both Python 2.x and 3.x
    def u(x):
        return x.decode('utf-8')
else:
    def u(x):
        return x
u('''
  cmappertools: Tools for the Python Mapper in C++

  Copyright © 2011–2015 Daniel Müllner <http://www.danifold.net>
''')
#import distutils.debug
#distutils.debug.DEBUG = 'yes'
from setuptools import setup, Extension

with open('cmappertools.cpp', 'r') as f:
    for line in f:
        if line.find('static char const __version__')==0:
            version = line.split('"')[1].split('"')[0]
            break

print('Version: ' + version)

setup(name='cmappertools',
      version=version,
      py_modules=[],
      description=('Optional helper module for the Python Mapper package '
                   'with fast, parallel C++ algorithms.'),
      long_description=('This is a companion package to `Python Mapper '
                   '<http://pypi.python.org/pypi/pythonmapper>`_. '
                   'It contains the optional helper module '
                   'with fast, parallel C++ algorithms.'),
      ext_modules=[Extension(
          'cmappertools',
          ['cmappertools.cpp'],
          language='c++',
          libraries=[] if os.name=='nt' else ['boost_thread', 'boost_chrono'],
          extra_compile_args=['/EHsc'] if os.name=='nt' else [],
      )],
      keywords=['Mapper'],
      author=u("Daniel Müllner"),
      author_email="daniel@danifold.net",
      license="GPLv3 <http://www.gnu.org/licenses/gpl.html>",
      classifiers = [
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Science/Research",
        "Development Status :: 5 - Production/Stable"
        ],
      url = 'http://danifold.net',
      )
