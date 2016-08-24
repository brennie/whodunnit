"""Setup whodunnit"""

import os
import sys

from setuptools import find_packages, setup
from setuptools.command.bdist_egg import bdist_egg


sys.path.insert(0, os.path.join(os.path.abspath('.'), 'server'))

from whodunnit import VERSION  # noqa


setup(
    name='whodunnit',
    version=VERSION,
    description='A simple to use progress tracker for teams.',
    url='https://github.com/brennie/whodunnit',
    author='Barret Rennie',
    author_email='barret@brennie.ca',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: Python 3.5',
    ],
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'whodunnit-server = whodunnit.commands.serve:main',
        ],
    },
)
