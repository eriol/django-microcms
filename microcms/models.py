# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.flatpages.models import FlatPage

class Meta(models.Model):
    flatpage = models.OneToOneField(FlatPage)
    links = models.ManyToManyField(FlatPage, related_name='superpages')

    def __unicode__(self):
        return self.flatpage.title
