# Generated by Django 3.1.13 on 2021-09-06 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0039_auto_20210906_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.autosearch'),
        ),
    ]