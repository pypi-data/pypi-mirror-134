from setuptools import setup, find_packages
import pathlib

import setuptools


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='simu',
    version='0.0.1',
    description='a simulation data generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/uncle-lv/simu',
    author='uncle-lv',
    author_email='uncle.lv@outlook.com',
    keywords='mock, test, random',
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    project_urls={
        'Bug Reports': 'https://github.com/uncle-lv/simu/issues',
        'Source': 'https://github.com/uncle-lv/simu',
    },
)