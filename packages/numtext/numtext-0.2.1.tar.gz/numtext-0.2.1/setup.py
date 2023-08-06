#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Sumanth",
    author_email='sumanthreddystar@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Package to convert number to text",
    entry_points={
        'console_scripts': [
            'numtext=numtext.cli:main',
        ],
    },
    install_requires=requirements,
    long_description_content_type='text/markdown',
    long_description=readme ,
    include_package_data=True,
    keywords='numtext',
    name='numtext',
    packages=find_packages(include=['numtext', 'numtext.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/insumanth/numtext',
    version='0.2.1',
    zip_safe=False,
)
