# Generated by Django 3.1.13 on 2021-09-05 14:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20210905_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrequest',
            name='pickup',
            field=models.DateField(default=datetime.datetime(2021, 9, 5, 14, 45, 28, 851, tzinfo=utc), null=True, verbose_name='Pickup Date'),
        ),
    ]