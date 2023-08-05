# -*- coding: latin-1 -*-

#!/usr/bin/env python

from distutils.core import setup

with open('README') as file:
    long_description = file.read()

setup(name='textmodel',
      version='0.3.2',
      description = \
          'A data type holding rich text data (textmodel).',
      long_description = long_description,
      author='C. Ecker',
      author_email='textmodelview@gmail.com',
      url='https://pypi.python.org/pypi/textmodel/',
      license='See file LICENSE',
      packages=['textmodel'],
      platforms = ['any'],
     )

