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
        'archive/subapps',
        'archive/api',
        'archive/routes'
        ],
    platforms='any',
    scripts=[],
    license='LICENSE',
    install_requires=[
        'waltz >= 0.1.7',
        'requests >= 1.2.3',
        'beautifulsoup',
        'markdown',
    ],
    description="Search Engine redesign concept for archive.org",
    long_description=open('README.md').read(),
)
