# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as StockFlatPageAdmin
from django.contrib.sites.models import Site

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

admin.site.unregister(FlatPage)

admin.site.register(FlatPage, FlatPageAdmin)
