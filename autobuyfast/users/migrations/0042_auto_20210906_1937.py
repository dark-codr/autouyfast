# Generated by Django 3.1.13 on 2021-09-06 18:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_auto_20210906_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrequest',
            name='pickup',
            field=models.DateField(default=datetime.datetime(2021, 9, 6, 18, 37, 0, 614432, tzinfo=utc), null=True, verbose_name='Pickup Date'),
        ),
    ]
