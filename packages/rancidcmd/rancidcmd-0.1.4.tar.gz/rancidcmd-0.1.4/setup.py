# -*- coding: utf-8 -*-

"""Racndicmd setup.py."""

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os
import sys


class Tox(TestCommand):

    """Tox."""

    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        """Init."""
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        """Finalize."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Run."""
        import tox
        import shlex
        if self.tox_args:
            errno = tox.cmdline(args=shlex.split(self.tox_args))
        else:
            errno = tox.cmdline(self.tox_args)
        sys.exit(errno)


classifiers = [
    "Development Status :: 3 - Alpha",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: System :: Networking",
    "Topic :: System :: Networking :: Monitoring",
    "Topic :: Utilities",
]


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = ['Sphinx']
with open('requirements.txt', 'w') as _file:
    _file.write('\n'.join(requires))

EXCLUDE_FROM_PACKAGES = []

setup(
    name="rancidcmd",
    version="0.1.4",
    description='Rancid Command Wrapper Tool',
    long_description=README,
    author='Toshikatsu Murakoshi',
    author_email='mtoshi.g@gmail.com',
    url='https://github.com/mtoshi/rancidcmd',
    license='MIT',
    classifiers=classifiers,
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    py_modules=['rancidcmd'],
    install_requires=requires,
    include_package_data=True,
    tests_require=['tox'],
    cmdclass={'test': Tox},
)
