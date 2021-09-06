# Generated by Django 3.1.13 on 2021-09-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0023_auto_20210904_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autosearch',
            name='car_drive_train',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Car Drive Train'),
        ),
        migrations.AlterField(
            model_name='autosearch',
            name='car_engine',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Car Engine'),
        ),
        migrations.AlterField(
            model_name='autosearch',
            name='car_ext_color',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Car Ext Color'),
        ),
        migrations.AlterField(
            model_name='autosearch',
            name='car_fuel_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Car Fuel Type'),
        ),
        migrations.AlterField(
            model_name='autosearch',
            name='car_int_color',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Car Int Color'),
        ),
        migrations.AlterField(
            model_name='autosearch',
            name='car_transmission',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Car Transmission'),
        ),
        migrations.AlterField(
            model_name='autosearch',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Car Title'),
        ),
    ]