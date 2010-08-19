# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as StockFlatPageAdmin
from django.contrib.sites.models import Site

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
    inlines = [MetaInline]

    class Media:
        js = [settings.TINYMCE_URL, settings.TINYMCE_SETUP_URL]

admin.site.unregister(FlatPage)

admin.site.register(FlatPage, FlatPageAdmin)
