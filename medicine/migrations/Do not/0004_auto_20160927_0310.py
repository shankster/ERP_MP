# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_auto_20160926_0332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='s_no',
            new_name='serial_no',
        ),
        migrations.AddField(
            model_name='medicine',
            name='stock_units',
            field=models.IntegerField(default=0),
        ),
    ]
