# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _


class Page(FlatPage):
    links = models.ManyToManyField('Page', related_name='superpages',
                                   blank=True, null=True)
    author = models.ForeignKey(User, verbose_name=_('author'))
    pub_date = models.DateTimeField(_('publication date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('last update date'), auto_now=True)
    # Fields for Search Engine Optimization
    meta_keywords = models.CharField(_('meta keywords'), blank=True,
                                     max_length=255)
    meta_description = models.CharField(_('meta description'), blank=True,
                                        max_length=255)

    def __unicode__(self):
        return self.title
