# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.flatpages.models import FlatPage

class Extra(models.Model):
    flatpage = models.OneToOneField(FlatPage)
    links = models.ManyToManyField(FlatPage, related_name='superpages',
                                   blank=True, null=True)

    def __unicode__(self):
        return self.flatpage.title
