# Generated by Django 3.1.13 on 2021-09-04 19:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210904_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrequest',
            name='pickup',
            field=models.DateField(default=datetime.datetime(2021, 9, 4, 19, 41, 20, 85722, tzinfo=utc), null=True, verbose_name='Pickup Date'),
        ),
    ]