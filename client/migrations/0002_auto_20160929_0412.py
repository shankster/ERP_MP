# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email_id',
            field=models.EmailField(default='Null', max_length=254),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(default='Null', max_length=100),
        ),
    ]
