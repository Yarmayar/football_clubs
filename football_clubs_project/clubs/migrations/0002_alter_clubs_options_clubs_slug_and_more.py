# Generated by Django 4.2.1 on 2023-12-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clubs',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddField(
            model_name='clubs',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='clubs',
            index=models.Index(fields=['-time_create'], name='clubs_clubs_time_cr_ffbf50_idx'),
        ),
    ]
