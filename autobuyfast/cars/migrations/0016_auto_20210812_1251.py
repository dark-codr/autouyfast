# Generated by Django 3.1.13 on 2021-08-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_auto_20210811_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock',
            field=models.CharField(blank=True, max_length=700, null=True, unique=True, verbose_name='Used or New Stock'),
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, unique=True, verbose_name='Production Year'),
        ),
    ]