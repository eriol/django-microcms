# -*- coding: utf-8 -*-
"""microcms.templatetags.microcms_tags module, some useful template tags for
microcms.

THIS SOFTWARE IS UNDER BSD LICENSE.
Copyright (c) 2010 Daniele Tricoli <eriol@mornie.org>

Read LICENSE for more informations.
"""
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def active_page(url, regex):
    """Check the current url with regex and return 'active' if matched.

    Avoid using this filter: better is to make use of CSS inheritance.
    """
    import re
    if re.search(regex, url):
        return 'active'
    else:
        return ''
