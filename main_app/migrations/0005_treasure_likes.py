# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_treasure_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
