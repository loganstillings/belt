# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_user_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pokehistory',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
