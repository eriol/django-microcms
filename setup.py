# -*- coding: utf-8 -*-
from distutils.core import setup

from microcms import VERSION

setup(name='microcms',
      version=VERSION,
      description='Simple flatpage enhancement',
      author='Daniele Tricoli',
      author_email='eriol@mornie.org',
      package_dir={'microcms': 'microcms'},
      packages=['microcms', 'microcms.conf', 'microcms.templatetags']
     )
