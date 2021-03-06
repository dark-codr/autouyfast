# Generated by Django 3.1.13 on 2021-08-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_auto_20210811_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='autosearch',
            name='car_sub_price',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=40, null=True, verbose_name='Car Old Price'),
        ),
        migrations.AlterField(
            model_name='autosearch',
            name='car_price',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=40, null=True, verbose_name='Car Main Price'),
        ),
    ]
