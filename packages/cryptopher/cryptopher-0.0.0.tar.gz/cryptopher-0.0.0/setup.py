#!/usr/bin/env python
# Copyright (c) Cryptopher.

import setuptools
import cryptopher

setup_info = dict(
    name = cryptopher.library_name,
    version = cryptopher.__version__,
    author='Cryptopher',
    author_email='cryptopher.trader@gmail.com',
    url='https://github.com/PesseCanoe/cryptopher',
    download_url='https://github.com/PesseCanoe/cryptopher/archive/v0_0_0.tar.gz',
    description = 'Cryptopher library',
    long_description = open('README.rst', 'r', encoding='utf-8').read(),
    long_description_content_type = 'text/markdown',
    install_requires=[
    "pandas",
    "plotly",
    "ccxt",
    "python-binance",
    ],
    license='MIT',
    python_requires='>=3.6',
    # Package info
    packages=[cryptopher.library_name] + [cryptopher.library_name + '.' + pkg for pkg in setuptools.find_packages(cryptopher.library_name)],
)

setuptools.setup(**setup_info)
