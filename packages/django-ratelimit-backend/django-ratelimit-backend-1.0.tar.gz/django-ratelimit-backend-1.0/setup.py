# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import ratelimitbackend

with open('README.rst', 'r') as f:
    long_description = f.read()


setup(
    name='django-ratelimit-backend',
    version=ratelimitbackend.__version__,
    author='Bruno Renié',
    author_email='bruno@renie.fr',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/brutasse/django-ratelimit-backend',
    license='BSD licence, see LICENCE file',
    description='Login rate-limiting at the auth backend level',
    long_description=long_description,
    install_requires=[
        'Django',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='runtests.runtests',
    zip_safe=False,
)
