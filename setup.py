#!/usr/bin/env python

from distutils.core import setup

setup(
  version="0.0.1",
  description="",
  author="Jacob D'Onofrio",
  author_email="jacob.donofrio@gmail.com",
  url='https://github.com/jdonofrio728/swaywm-bg-changer',
  scripts=["swaywm-bg-changer"],
  requires = [
    "daemon"
  ]
)
