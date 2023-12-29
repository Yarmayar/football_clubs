from django.contrib import admin
from .models import Clubs, Country


@admin.register(Clubs)
class ClubsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create', 'is_published', 'country']
    list_display_links = ['id', 'title']
    ordering = ['-time_create', 'title']
    list_editable = ['is_published', 'country']
    list_per_page = 10


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
