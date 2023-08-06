#!/usr/bin/env python3
#
#

import os
import sys

if sys.version_info.major < 3: print("you need to run KONING with python3") ; os._exit(1)

try: use_setuptools()
except: pass

try:
    from setuptools import setup
except Exception as ex: print(str(ex)) ; os._exit(1)

setup(
    name='koning',
    version='20',
    url='https://pikacode.com/bthate/koning',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description=""" KONING - niet de verboden maar de geboden vrucht. medicijnen eerst. """,
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    packages=['koning'],
    long_description=""" Recht op Leven. Recht op Vrijheid. Recht op Veiligheid.  """,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
