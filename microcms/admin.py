# -*- coding: utf-8 -*-
"""microcms.admin module, admin site configuration and options.

THIS SOFTWARE IS UNDER BSD LICENSE.
Copyright (c) 2010 Daniele Tricoli <eriol@mornie.org>

Read LICENSE for more informations.
"""
from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _


from microcms import settings as micro_settings
from microcms.models import Page


class PageForm(FlatpageForm):
    class Meta:
        model = Page


class PageAdmin(FlatPageAdmin):
    form = PageForm

    list_display = ('url', 'title', 'pub_date', 'modified_date',
                    'enable_comments', 'author')
    list_display_links = ('url', 'title')
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content')}),
        (_('Extra'),
         {'classes': ('collapse closed',), 'fields': ('links',)}),

        (_('Advanced options'),
         {'classes': ('collapse closed',),
          'fields': ('enable_comments',
                     'registration_required',
                     'template_name')}),

        (_('Search Engine Optimization'),
         {'classes': ('collapse closed',), 'fields': ('meta_keywords',
                                                      'meta_description')}),
    )

    formfield_overrides = {
        models.TextField:
            {'widget': forms.Textarea(attrs={'class': 'ckeditor'})},
    }

    class Media:
        css = {'all': micro_settings.MICROCMS_CUSTOM_CSS}
        js = [micro_settings.CKEDITOR_URL]

    def save_model(self, request, obj, form, change):

        # Get the site from settings
        site = Site.objects.get(id__exact=settings.SITE_ID)
        if not change:
            obj.author = request.user
        obj.save()
        obj.sites.add(site)

admin.site.unregister(FlatPage)
admin.site.register(Page, PageAdmin)
