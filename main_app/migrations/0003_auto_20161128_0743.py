# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treasure',
            name='img_url',
        ),
        migrations.AddField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='treasure_images'),
        ),
    ]
