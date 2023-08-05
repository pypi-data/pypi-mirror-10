import os
import re
from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `version.py`.
    """
    init_py = open(os.path.join(package, 'version.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name='docker-utils',
    version=get_version('utils'),
    description='Utilities for Docker',
    author='Andy McKay',
    author_email='andym@mozilla.com',
    license='BSD',
    install_requires=['docker-compose'],
    packages=['utils', 'utils/cmds'],
    entry_points={
        'console_scripts': [
            'docker-utils = utils.entry:entry'
        ]
    },
    url='https://github.com/andymckay/docker-utils',
    zip_safe=True,
)
