# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
def active_page(url, regex):
    """Check the current url with regex and return 'active' if matched."""
    import re
    if re.search(regex, url):
        return 'active'
    else:
        return ''
