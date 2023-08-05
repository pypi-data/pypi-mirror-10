#!/usr/bin/env python
# -*- coding: "utf-8" -*-

from setuptools import setup, find_packages
import sys
if "install" in sys.argv or "setup" in sys.argv or "sdist" in sys.argv:
    from confined import test_valid
    import unittest
    loader= unittest.TestLoader()
    suite=loader.loadTestsFromModule(test_valid)
    runner=unittest.TextTestRunner(verbosity=2)
    result=runner.run(suite)
    if  not result.wasSuccessful():
        raise Exception( "Test Failed")

setup(
        name='confined',
        version='0.1.4',
        author='Julien Tayon',
        author_email='julien@tayon.net',
        packages=['confined'],
        url='http://github.org/jul/confined',
        license="License :: OSI Approved :: BSD License",
        description="Sage templating language with bounded resource",
        long_description=open("README.rst").read(),
        install_requires=[ "check_arg",  ],
        classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Programming Language :: Python :: 2.7',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
)


