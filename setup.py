# -*- coding: utf-8 -*-
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
