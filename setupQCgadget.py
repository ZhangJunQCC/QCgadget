#!/usr/bin/python

#
#  To generate the exe file:
# python.exe setupQCgadget.py py2exe
#
#

from distutils.core import setup
import py2exe

setup(windows = ["e:\QCgadget\QCgadget.py"],
      data_files = [("bitmaps", ["logo.gif"])])
