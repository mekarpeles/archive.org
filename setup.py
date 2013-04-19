#-*- coding: utf-8 -*-

"""
    archive.org
    ~~~~~~~~~~~
    Dependencies

    Setup
    `````
    $ git clone github.com/mekarpeles/arvhive.org
    $ cd archive.org
    $ sudo pip install -e .
    $ sudo rm -rf build
"""

from distutils.core import setup

setup(
    name='archive.org',
    version='0.0.1',
    url='http://github.com/mekarpeles/archive.org',
    author='mek',
    author_email='michael.karpeles@gmail.com',
    packages=[
        'routes',
        'subapps'
        ],
    platforms='any',
    scripts=[],
    license='LICENSE',
    install_requires=[
        'waltz >= 0.1.68',
        'requests >= 1.1.0',
        'markdown',
    ],
    description="Search Engine redesign concept for archive.org",
    long_description=open('README.md').read(),
)
