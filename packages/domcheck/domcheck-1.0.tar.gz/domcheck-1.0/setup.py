#!/usr/bin/env python

import domcheck

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='domcheck',
    version=domcheck.__version__,
    description='Domain Ownership Checker',
    author='Olivier Poitrey',
    author_email='rs@dailymotion.com',
    url='https://github.com/rs/domcheck',
    keywords=["domain", "validation", "verification", "check", "ownership", "dns", "txt", "cname", "meta"],
    packages=['domcheck'],
    package_dir={'domcheck': 'domcheck'},
    install_requires=['dnspython'],
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Security',
    ]
 )

