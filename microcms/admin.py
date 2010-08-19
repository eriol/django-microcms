# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as StockFlatPageAdmin
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from microcms.conf import settings
from microcms.models import Meta

class MetaAdmin(admin.ModelAdmin):
    list_display = ('flatpage',)
    list_filter = ('flatpage',)
    ordering = ('flatpage',)
    search_fields = ('flatpage',)

admin.site.register(Meta, MetaAdmin)

class MetaInline(admin.StackedInline):
    model = Meta

class FlatPageAdmin(StockFlatPageAdmin):
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
    inlines = [MetaInline]

    class Media:
        js = [settings.TINYMCE_URL, settings.TINYMCE_SETUP_URL]

    def save_model(self, request, obj, form, change):
        # Get the site with the lower id
        site = Site.objects.order_by('id')[0]
        obj.save()
        obj.sites.add(site)

admin.site.unregister(FlatPage)

admin.site.register(FlatPage, FlatPageAdmin)
