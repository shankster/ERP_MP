# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-21 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='medicine_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]