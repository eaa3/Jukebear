# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-07 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jukebox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jukebox',
            name='songs',
            field=models.ManyToManyField(blank=True, to='jukebox.Song'),
        ),
    ]
