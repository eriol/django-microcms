# -*- coding: utf-8 -*-
from django.conf import settings

CKEDITOR_URL = getattr(settings, 'CKEDITOR_URL', 'ckeditor/ckeditor.js')
