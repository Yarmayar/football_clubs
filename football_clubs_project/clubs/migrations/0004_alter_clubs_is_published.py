# Generated by Django 4.2.1 on 2023-12-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_alter_clubs_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
