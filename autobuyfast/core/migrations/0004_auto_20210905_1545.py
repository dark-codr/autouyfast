# Generated by Django 3.1.13 on 2021-09-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210905_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='country_id',
        ),
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='region',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='sub_region',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]