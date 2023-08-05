import os
import sys

py_version = sys.version_info[:2]
if py_version < (3, 4):
    raise RuntimeError('ApiDaemon requires Python 3.4 or later')

from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
README = """ Pluggable daemon for wrapping external APIs and create own. """
CHANGES = ''

CLASSIFIERS = [
    'Natural Language :: English',
    'Operating System :: POSIX',
    "Programming Language :: Python :: 3.4",
]

path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ApiDaemon'))
daemon_version = open(os.path.join(path, 'version')).read().strip()
dist = setup(
    name='ApiDaemon',
    version=daemon_version,
    license='MIT-license',
    url='https://github.com/tsyganov-ivan/ApiDaemon',
    description="Daemon for wraps any external APIs",
    long_description=README + '\n\n' + CHANGES,
    classifiers=CLASSIFIERS,
    author="Ivan Tsyganov",
    author_email="tsyganov.ivan@gmail.com",
    packages=find_packages(),
    install_requires=[
        'requests',
        'AsyncVk==1.0-alpha',
        'Click',
        'PyYAML'
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'apidaemon = ApiDaemon.runner:main'
        ],
    },
)
