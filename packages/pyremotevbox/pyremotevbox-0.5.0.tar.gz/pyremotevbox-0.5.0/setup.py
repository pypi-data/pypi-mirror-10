#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyremotevbox',
    version='0.5.0',
    description='Python API to talk to a remote VirtualBox using VirtualBox WebService',
    long_description=readme + '\n\n' + history,
    author='Ramakrishnan G',
    author_email='rameshg87@gmail.com',
    url='https://github.com/rameshg87/pyremotevbox',
    packages=[ 'pyremotevbox', 'pyremotevbox.ZSI', 'pyremotevbox.ZSI.twisted',
               'pyremotevbox.ZSI.wstools', 'pyremotevbox.ZSI.generate' ],
    package_dir={'pyremotevbox': 'pyremotevbox',
                 'pyremotevbox.ZSI': 'pyremotevbox/ZSI',
                 'pyremotevbox.ZSI.twisted': 'pyremotevbox/ZSI/twisted',
                 'pyremotevbox.ZSI.wstools': 'pyremotevbox/ZSI/wstools',
                 'pyremotevbox.ZSI.generate': 'pyremotevbox/ZSI/generate'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache",
    zip_safe=False,
    keywords='pyremotevbox',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
