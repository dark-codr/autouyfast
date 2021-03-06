# Generated by Django 3.1.13 on 2021-09-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0032_auto_20210905_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autosearch',
            name='car_body',
            field=models.CharField(blank=True, choices=[('', 'all'), ('sedan', 'sedan'), ('coupe', 'coupe'), ('convertible', 'convertible'), ('wagon', 'wagon'), ('hatchback', 'hatchback'), ('passenger_van', 'passenger van'), ('suv', 'suv'), ('minivan', 'minivan'), ('pickup_truck', 'pickup truck'), ('cargo_van', 'cargo van')], default='sedan', max_length=15, null=True, verbose_name='Car Body'),
        ),
    ]
