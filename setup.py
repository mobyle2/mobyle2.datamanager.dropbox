# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    "dropbox"
    ]

setup(name='mobyle.data.manager.dropbox',
      version='0.1',
      description='mobyle plugin to DropBox',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Olivier Sallou',
      author_email='olivier.sallou@irisa.fr',
      url='https://github.com/osallou/mobyle2.datamanager.dropbox',
      keywords='DropBox data mobyle plugin',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="test",
      )

