#!/usr/bin/env python

from distutils.core import setup

setup(name='ReParser',
      version='1.4.1',
      description='Simple regex-based lexer/parser for inline markup',
      author='Michal Krenek (Mikos)',
      author_email='m.krenek@gmail.com',
      url='https://github.com/xmikos/reparser',
      license="MIT",
      py_modules=['reparser'],
      requires=['enum34'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing :: Markup'
      ])
