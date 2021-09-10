# Generated by Django 3.1.13 on 2021-09-10 03:05

import autobuyfast.users.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0046_auto_20210908_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrequest',
            name='pickup',
            field=models.DateField(default=datetime.datetime(2021, 9, 10, 3, 5, 16, 708551, tzinfo=utc), null=True, verbose_name='Pickup Date'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='banner_display',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Image should be cropped and sized 1280px X 300px', keep_meta=True, null=True, quality=75, size=[750, 430], upload_to=autobuyfast.users.models.banner_image),
        ),
    ]