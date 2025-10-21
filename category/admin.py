from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from category.models import Category


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'slug')
