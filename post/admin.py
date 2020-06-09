# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','created','category']
    list_filter = ['category__name']

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']

class TagModelAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category,CategoryModelAdmin)
admin.site.register(Tag,TagModelAdmin)
admin.site.register(Post,PostModelAdmin)