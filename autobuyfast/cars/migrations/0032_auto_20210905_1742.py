# Generated by Django 3.1.13 on 2021-09-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0031_auto_20210905_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autosearch',
            name='title',
            field=models.CharField(blank=True, max_length=700, null=True, verbose_name='Car Title'),
        ),
    ]