# Generated by Django 3.1.13 on 2021-09-05 16:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20210905_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrequest',
            name='pickup',
            field=models.DateField(default=datetime.datetime(2021, 9, 5, 16, 30, 1, 133796, tzinfo=utc), null=True, verbose_name='Pickup Date'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='Zipcode'),
        ),
    ]