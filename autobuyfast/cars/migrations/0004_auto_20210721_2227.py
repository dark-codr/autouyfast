# Generated by Django 3.1.13 on 2021-07-21 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20210721_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autosearch',
            name='car_dealer_rating',
        ),
        migrations.RemoveField(
            model_name='autosearch',
            name='car_dealer_reviews',
        ),
    ]
