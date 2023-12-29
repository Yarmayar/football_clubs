from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Clubs.Status.PUBLISHED)


class Clubs(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft'  # 0 будет записываться в БД, текст будет отображаться в виджетах
        PUBLISHED = 1, 'Published'

    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Содержание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                                     default=Status.DRAFT, verbose_name='Статус')
    country = models.ForeignKey('Country', on_delete=models.PROTECT, related_name='clubs', verbose_name='Страна')
    tags = models.ManyToManyField('TagClub', blank=True, related_name='tags')

    objects = models.Manager()
    published = PublishedManager()
    coach = models.OneToOneField('Coach', on_delete=models.SET_NULL, null=True, blank=True, related_name='job')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]
        verbose_name = 'Футбольный клуб'
        verbose_name_plural = 'Футбольные клубы'

    def get_absolute_url(self):
        return reverse('club', kwargs={'club_slug': self.slug})

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Страна')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def get_absolute_url(self):
        return reverse('country', kwargs={'country_slug': self.slug})


class TagClub(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Coach(models.Model):
    name = models.TextField(max_length=255)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name
