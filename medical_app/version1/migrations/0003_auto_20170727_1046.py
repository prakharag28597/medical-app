# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-27 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version1', '0002_auto_20170727_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.CharField(max_length=25),
        ),
    ]
