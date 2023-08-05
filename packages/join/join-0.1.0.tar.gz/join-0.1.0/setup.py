#!/bin/python

from distutils.core import setup

with open('README.rst') as readme:
    long_description = readme.read()

with open('LICENSE.txt') as license_file:
    license = license_file.read()

setup(name='join',
      packages=['join'],
      version='0.1.0',
      description='SQL-style joins for iterables.',
      long_description=long_description,
      license=license,
      author='Stuart Owen',
      author_email='stuart.owen@gmail.com',
      url='https://github.com/StuartAxelOwen/join',
      download_url='https://github.com/StuartAxelOwen/join/archive/0.1.zip',
      keywords=['join', 'joins', 'merge', 'merges', 'list join', 'iterable join'],
      )
