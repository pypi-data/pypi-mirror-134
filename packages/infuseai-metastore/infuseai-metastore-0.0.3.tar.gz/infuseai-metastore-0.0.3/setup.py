#!/usr/bin/env python
import os
from distutils.core import setup

from setuptools import find_packages  # type: ignore


def _get_version():
    version_file = os.path.normpath(os.path.join(os.path.dirname(__file__), 'metastore', 'VERSION'))
    with open(version_file) as fh:
        version = fh.read().strip()
        return version


setup(name='infuseai-metastore',
      version=_get_version(),
      description='MetaStore',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      author='qrtt1',
      author_email='qrtt1@infuseai.io',
      url='https://github.com/InfuseAI/mm-only-details/issues',
      python_requires=">=3.6",
      packages=find_packages(),
      install_requires=['kafka-python', 'boto3', 'requests', 'pandas'],
      extras_require={
          'dev': ['twine'],
      },
      project_urls={
          "Bug Tracker": "https://github.com/InfuseAI/primehub/issues",
      },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Development Status :: 4 - Beta"
      ],
      package_data={
          'metastore': ['*.json', 'VERSION']
      })
