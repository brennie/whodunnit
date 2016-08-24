"""Setup whodunnit"""

import os
import subprocess

from distutils.command.build import build
from distutils.errors import DistutilsError
from setuptools import Command, find_packages, setup
from setuptools.command.bdist_egg import bdist_egg

from whodunnit import VERSION


class WebpackError(DistutilsError):
    """An error that occurred within webpack."""


class BDistEggCommand(bdist_egg):
    """Create an .egg

    This will run webpack beforehand to ensure the client files are up-to-date.
    """

    def run(self):
        """Create the .egg."""
        self.run_command('webpack')
        super().run()


class BuildCommand(build):
    """Build the package.

    This will run webpack beforehand to ensure the client files are up-to-date.
    """

    def run(self):
        """Build the package."""
        self.run_command('webpack')
        super().run()


class WebpackCommand(Command):
    """Build the client code with webpack."""

    user_options = [
        ('development', None, 'Build a development package instead of production.'),
    ]

    description = 'Build JavaScript, HTML, and CSS files with webpack.'

    def initialize_options(self):
        """Initialize command options."""
        self.development = False

    def finalize_options(self):
        """Finalize command options.

        This is intentionally a no-op.
        """

    def run(self):
        """Run webpack."""
        env = os.environ.copy()
        if self.development:
            env['NODE_ENV'] = 'development'
        else:
            env['NODE_ENV'] = 'production'

        result = subprocess.run(['webpack'], env=env)
        if result.returncode != 0:
            raise WebpackError()


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
    include_package_data=True,
    install_requires=[
        'aiohttp',
        'aiohttp-index',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'whodunnit-server = whodunnit.commands.serve:main',
        ],
    },
    cmdclass={
        'bdist_egg': BDistEggCommand,
        'build': BuildCommand,
        'webpack': WebpackCommand,
    }
)
