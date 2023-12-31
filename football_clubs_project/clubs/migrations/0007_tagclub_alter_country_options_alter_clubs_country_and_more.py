# Generated by Django 4.2.1 on 2023-12-28 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_alter_clubs_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='clubs',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clubs', to='clubs.country'),
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['name'], name='clubs_count_name_439afd_idx'),
        ),
        migrations.AddField(
            model_name='clubs',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='clubs.tagclub'),
        ),
    ]
