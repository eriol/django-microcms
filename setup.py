# -*- coding: utf-8 -*-
"""microcms setup file.

THIS SOFTWARE IS UNDER BSD LICENSE.
Copyright (c) 2010 Daniele Tricoli <eriol@mornie.org>

Read LICENSE for more informations.
"""
from setuptools import setup, find_packages

from microcms import VERSION

setup(
    name='microcms',
    version='.'.join(str(v) for v in VERSION),
    description='Minimalistic flatpage enhancement.',
    author='Daniele Tricoli',
    author_email='eriol@mornie.org',
    packages=find_packages(),
    package_data = {
        'microcms': [
            'locale/*/LC_MESSAGES/*',
            'templates/flatpages/*',
        ],
    },
)
