# -*- coding: utf-8 -*-
"""microcms.models module, Page the core model of microcms.

THIS SOFTWARE IS UNDER BSD LICENSE.
Copyright (c) 2010-2012 Daniele Tricoli <eriol@mornie.org>

Read LICENSE for more informations.
"""
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _


class Page(FlatPage):
    author = models.ForeignKey(User, verbose_name=_('author'))
    pub_date = models.DateTimeField(_('publication date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('last modified date'),
                                         auto_now=True)
    links = models.ManyToManyField('Page', blank=True, null=True,
                                   related_name='superpages',
                                   verbose_name=_('links'))
    # Fields for Search Engine Optimization
    meta_keywords = models.CharField(_('meta keywords'), blank=True,
                                     help_text=_('Key words of the page. '
                                                 'Max 255 characters.'),
                                     max_length=255)
    meta_description = models.CharField(_('meta description'), blank=True,
                                        help_text=_('A brief description of '
                                                    'the page. '
                                                    'Max 255 characters.'),
                                        max_length=255)

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')

    def __unicode__(self):
        return self.title
