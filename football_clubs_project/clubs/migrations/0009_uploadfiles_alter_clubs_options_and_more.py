# Generated by Django 4.2.1 on 2024-01-03 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0008_coach_clubs_coach'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads_model')),
            ],
        ),
        migrations.AlterModelOptions(
            name='clubs',
            options={'ordering': ['-time_create'], 'verbose_name': 'Футбольный клуб', 'verbose_name_plural': 'Футбольные клубы'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name'], 'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterField(
            model_name='clubs',
            name='content',
            field=models.TextField(blank=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clubs', to='clubs.country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Draft'), (True, 'Published')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время обновления'),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
