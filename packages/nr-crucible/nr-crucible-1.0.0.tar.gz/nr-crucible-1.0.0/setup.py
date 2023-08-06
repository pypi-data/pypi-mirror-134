#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst', encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', encoding="utf-8") as history_file:
    history = history_file.read()

requirements = ['python-docx>=0.8.11']

test_requirements = ['pytest>=3', ]

setup(
    author="John Bisignano",
    author_email='jbiz@pm.me',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Crucible tools",
    entry_points={
        'console_scripts': [
            'crucible=crucible.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords='crucible',
    name='nr-crucible',
    packages=find_packages(include=['crucible', 'crucible.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/johnnyrockets/crucible',
    version='1.0.0',
    zip_safe=False,
)
