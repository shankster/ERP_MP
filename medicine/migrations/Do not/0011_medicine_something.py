# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0010_auto_20160929_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='something',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
