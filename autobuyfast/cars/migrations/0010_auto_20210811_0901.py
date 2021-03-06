# Generated by Django 3.1.13 on 2021-08-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_auto_20210811_0847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autosearch',
            old_name='car_title',
            new_name='title',
        ),
        migrations.AddField(
            model_name='autosearch',
            name='slug',
            field=models.SlugField(blank=True, max_length=800, null=True, unique=True),
        ),
    ]
