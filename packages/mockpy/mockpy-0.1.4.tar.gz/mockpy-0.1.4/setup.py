#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('Readme.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "mock",
    "cherrypy",
    "termcolor",
    "watchdog",
    "mitmproxy"
]

test_requirements = [
    "mock",
    "termcolor"
]

setup(
    name='mockpy',
    version='0.1.4',
    description="Mockpy is an work in progress open source tool to quickly create mock servers. Mockpy is inspired from wiremock and uses libmproxy for the proxy functionality",
    long_description=readme + '\n\n' + history,
    author="Omar Abdelhafith",
    author_email='o.arrabi@me.com',
    url='https://github.com/oarrabi/mockpy',
    packages=[
        'mockpy',
        "mockpy.core",
        "mockpy.models",
        "mockpy.utils",
        "mockpy.status",
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='mockpy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'mockpy=mockpy.mockpy:start',
        ],
    },
)
