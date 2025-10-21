from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(TranslationAdmin):
    search_fields = ('full_name',)
    list_display = ('id', 'full_name', 'profession', 'speciality')
