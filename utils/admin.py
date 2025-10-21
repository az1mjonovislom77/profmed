from django.contrib import admin

from .models import Location, SocialMedia, HomepageStats, FooterStats


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'region')


@admin.register(SocialMedia)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')


@admin.register(HomepageStats)
class HomepageStatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'happy_patients', 'wards', 'awards', 'ambulances')


@admin.register(FooterStats)
class FooterStatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctors', 'experience', 'awards', 'successfully_operations')
