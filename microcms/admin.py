# -*- coding: utf-8 -*-
"""microcms.admin module, admin site configuration and options.

THIS SOFTWARE IS UNDER BSD LICENSE.
Copyright (c) 2010-2012 Daniele Tricoli <eriol@mornie.org>

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


from microcms import settings as microcms_settings
from microcms.models import Page


class PageForm(FlatpageForm):
    class Meta:
        model = Page


class PageAdmin(FlatPageAdmin):
    form = PageForm

    list_display = ('url', 'title', 'pub_date', 'modified_date',
                    'enable_comments', 'author')
    list_display_links = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required',
                   'author', 'pub_date', 'modified_date')
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content')}),
        (_('Extra'),
         {'classes': ('collapse closed',), 'fields': ('links',)}),

        (_('Advanced options'),
         {'classes': ('collapse closed',),
          'fields': ('enable_comments',
                     'registration_required',
                     'template_name',
                     'sites')}),

        (_('Search Engine Optimization'),
         {'classes': ('collapse closed',), 'fields': ('meta_keywords',
                                                      'meta_description')}),
    )

    formfield_overrides = {
        models.TextField:
            {'widget': forms.Textarea(attrs={'class': 'ckeditor'})},
    }

    class Media:
        css = {'all': microcms_settings.MICROCMS_CUSTOM_CSS}
        js = [microcms_settings.CKEDITOR_URL]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'sites':
            kwargs["initial"] = [Site.objects.get_current()]
        return super(PageAdmin, self).formfield_for_manytomany(db_field,
                                                               request,
                                                               **kwargs)

    def save_model(self, request, obj, form, change):

        if not change:
            obj.author = request.user
        obj.save()

admin.site.unregister(FlatPage)
admin.site.register(Page, PageAdmin)
