# Generated by Django 3.1.13 on 2021-09-05 13:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210905_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrequest',
            name='pickup',
            field=models.DateField(default=datetime.datetime(2021, 9, 5, 13, 48, 7, 908407, tzinfo=utc), null=True, verbose_name='Pickup Date'),
        ),
    ]