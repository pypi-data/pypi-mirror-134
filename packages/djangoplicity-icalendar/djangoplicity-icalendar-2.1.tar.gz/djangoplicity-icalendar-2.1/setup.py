#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='djangoplicity-icalendar',
      package_dir={'': 'src'},
      packages=['icalendar'],
      version='2.1',
      long_description = open('README.rst').read(),
      # metadata for upload to PyPI
      author='MaxM',
      author_email='maxm@mxm.dk',
      description='iCalendar parser/generator',
      license='GPL2.1',
      keywords='calendar icalendar',
      url='https://github.com/djangoplicity/djangoplicity-icalendar',
      download_url = 'https://github.com/djangoplicity/djangoplicity-icalendar/archive/refs/tags/2.1.tar.gz',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: OS Independent'],
      platforms='All',
      )