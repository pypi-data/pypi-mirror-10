
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        super().finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup_args = dict(
    name='pyvodb',
    version='0.0.1',
    packages=['pyvodb'],

    description="""Database of Pyvo meetups""",
    author='Petr Viktorin',
    author_email='encukou@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    install_requires=[
        'blessings >= 1.6, < 2.0',
        'sqlalchemy >= 1.0, < 2.0',
        'PyYAML >= 3.11, < 4.0',
    ],

    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)


if __name__ == '__main__':
    setup(**setup_args)
