#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2015 John Törnblom

import logging
import unittest
import sys

try:
    from setuptools import setup
    from setuptools import Command
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup
    from distutils.core import Command
    from distutils.command.install import install

import rsl


logging.basicConfig(level=logging.DEBUG)


class InstallCommand(install):
    
    def run(self):
        rsl.parse_text('', '')
        install.run(self)

        
class TestCommand(Command):
    description = "Execute unit tests"
    user_options = []

    def initialize_options(self):
        pass
    
    def finalize_options(self):
        pass

    def run(self):
        suite = unittest.TestLoader().discover('tests')
        runner = unittest.TextTestRunner(verbosity=2, buffer=True)
        exit_code = not runner.run(suite).wasSuccessful()
        sys.exit(exit_code)


setup(name='pyrsl',
      version=rsl.version.release,
      description='Interpreter for the Rule Specification Language (RSL)',
      author='John Törnblom',
      author_email='john.tornblom@gmail.com',
      url='https://github.com/john-tornblom/pyrsl',
      license='GPLv3',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Interpreters',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4'],
      keywords='rsl xtuml bridgepoint',
      platforms=["Linux"],
      packages=['rsl'],
      requires=['ply', 'xtuml'],
      cmdclass={'install': InstallCommand, 'test': TestCommand}
      )

