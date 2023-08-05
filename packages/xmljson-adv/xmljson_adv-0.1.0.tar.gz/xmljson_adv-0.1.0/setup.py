#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io

import setuptools

with io.open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with io.open('HISTORY.rst', encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setuptools.setup(
    name='xmljson_adv',
    version='0.1.0',
    description='Converts XML into JSON/Python dicts/arrays and vice-versa. (Modified Version)',
    long_description=readme + '\n\n' + history,
    author='ret2happy',
    author_email='',
    url='https://github.com/sanand0/xmljson',
    packages=[
        'xmljson_adv',
    ],
    package_dir={'xmljson_adv':
                 'xmljson_adv'},
    include_package_data=True,
    install_requires=[],
    license='MIT',
    zip_safe=False,
    keywords='xmljson_adv',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',    # For collections.Counter
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='tests',
    tests_require=['lxml'],
    entry_points={
        'console_scripts': [
            'xml2json = xmljson_adv.__main__:main'
        ]
    }
)
