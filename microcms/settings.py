# -*- coding: utf-8 -*-
from django.conf import settings

CKEDITOR_URL = getattr(settings, 'CKEDITOR_URL', 'ckeditor/ckeditor.js')
# Default value for custom css is an empty tuple to give greater flexibility.
# In yours settings.py you should use:
# MICROCMS_CUSTOM_CSS = ('custom-css.css',) # single css file
# MICROCMS_CUSTOM_CSS = ('custom-css1.css', 'custom-css2.css') # multiple css
MICROCMS_CUSTOM_CSS = getattr(settings, 'MICROCMS_CUSTOM_CSS', ())
