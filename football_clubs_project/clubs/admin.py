from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Clubs, Country


class HaveCoach(admin.SimpleListFilter):
    title = 'Статус клубов'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('with_coach', 'Есть тренер'),
            ('vacancy', 'В поисках тренера')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'with_coach':
            return queryset.filter(coach__isnull=False)
        elif self.value() == 'vacancy':
            return queryset.filter(coach__isnull=True)


@admin.register(Clubs)
class ClubsAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'logo', 'club_logo', 'country', 'tags', 'coach']
    readonly_fields = ['club_logo']  # для отображения полей без возможности редактировать их,
    # при использовании поля в prepopulated_fields его нельзя оставить нередактируемым
    # exclude = ['title']  # альтернатива field, отображать все, кроме перечисленого
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'club_logo', 'time_create', 'is_published', 'country']
    list_display_links = ['title']
    ordering = ['-time_create', 'title']
    list_editable = ['is_published', 'country']
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'country__name']
    list_filter = [HaveCoach, 'country__name', 'is_published']
    filter_horizontal = ['tags']
    save_on_top = True

    @admin.display(description='Current logo', ordering='logo')
    def club_logo(self, club: Clubs):
        if club.logo:
            return mark_safe(f'<img src="{club.logo.url}" width=50>')
        return 'Without logo'

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
