# Generated by Django 3.1.13 on 2021-09-08 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0045_auto_20210908_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='carcompare',
            name='slug',
            field=models.SlugField(blank=True, default='result', max_length=800, null=True, unique=True),
        ),
    ]
