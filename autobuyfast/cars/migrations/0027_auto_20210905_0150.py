# Generated by Django 3.1.13 on 2021-09-05 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0026_remove_autosearch_car_def_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autosearch',
            name='car_stock',
            field=models.CharField(blank=True, choices=[('used', 'used'), ('new', 'new'), ('certified', 'certified')], default='used', max_length=25, null=True, verbose_name='Car Stock Type'),
        ),
        migrations.AlterField(
            model_name='autosearch',
            name='car_url',
            field=models.CharField(blank=True, max_length=700, null=True, verbose_name='Car Detail Link'),
        ),
    ]