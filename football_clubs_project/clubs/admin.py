from django.contrib import admin, messages
from .models import Clubs, Country


@admin.register(Clubs)
class ClubsAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_create', 'is_published', 'country', 'brief_info']
    list_display_links = ['title']
    ordering = ['-time_create', 'title']
    list_editable = ['is_published', 'country']
    list_per_page = 10
    actions = ['set_published', 'set_draft']

    @admin.display(description='Содержание', ordering='content')
    def brief_info(self, club: Clubs):
        return f'{len(club.content)} символов'

    @admin.action(description='Опубликовать записи выбранных клубы')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Clubs.Status.PUBLISHED)
        # метод update возвращает количество записей
        self.message_user(request, f'Опубликовано записей: {count}')

    @admin.action(description='Снять с публикации записи выбранных клубов')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Clubs.Status.DRAFT)
        # метод update возвращает количество записей
        self.message_user(request, f'Записи сняты c публикации в количестве: {count}', messages.WARNING)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
