#!/usr/bin/env python

from os.path import abspath, dirname, join
from setuptools import setup, find_packages

ROOT = dirname(abspath(__file__))

version_file = join(ROOT, 'ATXLibrary', 'version.py')
exec(compile(open(version_file).read(), version_file, 'exec'))

setup(name='robotframework-atxlibrary',
      version=VERSION,
      description='Robot Framework Mobile app testing library for ATX Client Android & iOS',
      long_description=open(join(ROOT, 'README.rst')).read(),
      author='Peng Yuan',
      author_email='ggfor826079925@gmail.com',
      url='',
      license='Apache License 2.0',
      keywords='robotframework testing testautomation mobile atx webdriver app android ios',
      platforms='any',
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing",
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation',
          'Programming Language :: Python :: Implementation :: CPython',
      ],
      # setup_requires=[
      #     "pytest-runner"
      # ],
      install_requires=[
          'atx >= 1.2.1.dev12',
          'decorator >= 4.4.0',
          'robotframework >= 3.1.2',
          'docutils >= 0.14',
          'kitchen >= 1.2.6',
          'six >= 1.12.0'
      ],
      # tests_require=[
      #     'mock >= 2.0.0',
      #     'pytest-cov >= 2.5.1',
      #     'pytest-xdist >= 1.16.0',
      #     'pytest-pythonpath >= 0.7.1',
      #     'pytest >= 3.1.0',
      #     'six >= 1.10.0'
      # ],
      # packages=find_packages(exclude=["demo", "docs", "tests", ]),
      include_package_data=True,
      )
