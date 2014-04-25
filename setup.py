from distutils.core import setup
import nbt
import py2exe
import sys

if sys.args[1] == "py2exe":
    setup(console=['region-fixer.py'], data_files=['COPYING.txt','README.rst','CONTRIBUTORS.txt'])
else:
    print "Use \'python setup.py py2exe\' to build a windows executable."
