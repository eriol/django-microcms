# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as OldFlatPageAdmin
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _

from microcms.conf import settings
from microcms.models import Extra

class ExtraAdmin(admin.ModelAdmin):
    list_display = ('flatpage',)
    list_filter = ('flatpage',)
    ordering = ('flatpage',)
    search_fields = ('flatpage',)

admin.site.register(Extra, ExtraAdmin)

class ExtraInline(admin.StackedInline):
    model = Extra

class FlatPageAdmin(OldFlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content')}),
        (_('Advanced options'),
         {'classes': ('collapse closed',),
          'fields': ('enable_comments',
                     'registration_required',
                     'template_name')
         }
        ),
    )
    inlines = [ExtraInline]

    formfield_overrides = {
        models.TextField:
            {'widget': forms.Textarea(attrs={'class':'ckeditor',})},
    }

    class Media:
        js = [settings.CKEDITOR_URL]

    def save_model(self, request, obj, form, change):
        # Get the site with the lower id
        site = Site.objects.order_by('id')[0]
        obj.save()
        obj.sites.add(site)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
