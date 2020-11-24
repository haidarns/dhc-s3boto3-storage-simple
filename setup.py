#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import setup
# from setuptools.command.test import test as testCommand

# import s3boto3_storage_simple

setup(
    name='dhc_s3boto3_storage_simple',
    version='0.0.1',
    # description=health_check_plus.__description__,
    long_description='Django package to improve usage of django-health-check library.',
    # author=health_check_plus.__author__,
    # author_email=health_check_plus.__email__,
    # url=health_check_plus.__url__,
    packages=[
        'dhc_s3boto3_storage_simple',
    ],
    include_package_data=True,
    install_requires=['django-health-check==3.16.1'],
    # license=health_check_plus.__license__,
    zip_safe=False,
    keywords='python, django, health, check, network, service',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    # test_suite='tests',
    # tests_require=['tox', 'Django'],
    # cmdclass={'test': Tox},
)