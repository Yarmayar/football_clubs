# Generated by Django 4.2.1 on 2024-01-09 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='clubs',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clubs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clubs',
            name='coach',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job', to='clubs.coach'),
        ),
        migrations.AddField(
            model_name='clubs',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clubs', to='clubs.country', verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='clubs',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='clubs.tagclub'),
        ),
        migrations.AddIndex(
            model_name='clubs',
            index=models.Index(fields=['-time_create'], name='clubs_clubs_time_cr_ffbf50_idx'),
        ),
    ]