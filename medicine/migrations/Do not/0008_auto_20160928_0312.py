# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import medicine.models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0007_auto_20160927_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='serial_no',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]