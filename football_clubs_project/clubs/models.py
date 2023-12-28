from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Clubs.Status.PUBLISHED)


class Clubs(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft'  # 0 будет записываться в БД, текст будет отображаться в виджетах
        PUBLISHED = 1, 'Published'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, related_name='clubs')
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

    def get_absolute_url(self):
        return reverse('club', kwargs={'club_slug': self.slug})


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
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
