# Generated by Django 3.1.13 on 2021-08-10 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210806_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='car_price_notif',
            field=models.BooleanField(default=False, verbose_name='Send Email When Saved car price has been reduced?'),
        ),
        migrations.AddField(
            model_name='user',
            name='car_sold_notif',
            field=models.BooleanField(default=False, verbose_name='Send Email When Saved car is sold?'),
        ),
        migrations.AddField(
            model_name='user',
            name='newsletter_notif',
            field=models.BooleanField(default=False, verbose_name='Subscribe to Newsletter?'),
        ),
        migrations.AddField(
            model_name='user',
            name='search_notif',
            field=models.BooleanField(default=False, verbose_name='Send Email When Saved Search is deleted?'),
        ),
    ]
