import pathlib
import os
import subprocess

from setuptools import find_packages, setup

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
with open(here / 'README.md', 'r') as readme:
    long_description = readme.read()


def get_latest_tag():
    os.system('git fetch --tags')
    return subprocess.check_output(['git', 'describe', '--tags']).decode().strip()


def bump_patch(vers):
    major, minor, patch = vers.split('.')
    if not patch.isnumeric():
        return vers
    bumped_patch = str(int(patch) + 1)
    return '.'.join([major, minor, bumped_patch])


VERSION = '0.0.0'
if 'DEPLOY' in os.environ:
    VERSION = os.environ['GITHUB_REF'].split('/')[-1]


setup(
    name='shapesorter',
    version=VERSION,
    description='A lightweight templating language for any kind of text.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/atraders/temp-later',
    author='@genziano',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='devops, template',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=['pyyaml~=6.0'],
    extras_require={'dev': ['flake8', 'pytest', 'mypy', 'isort', 'types-PyYAML ~= 5.4.8'],},
    entry_points={
        "console_scripts": ["shapesort=fillform.shapesorter:main"],
    },
)
