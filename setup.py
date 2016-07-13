#Python Script to install the biojs2IPython
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='biojs2IPython',
    version='0.1.0',
    description='Application to port biojs components to IPython',
    author='Rohan Jaswal',
    author_email='rohanjaswal2507@gmail.com',
    #url='https://github.com/rohanjaswal2507/biojs2IPython',
    packages=['biojs'],
    install_requires=['ipywidgets'],
    include_package_data=True,
    license="Apache",
    zip_safe=False,
    keywords='biojs2IPython ipython jupyter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
