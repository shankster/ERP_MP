# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20160929_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact_number',
            field=models.CharField(default='', max_length=10, help_text='Enter STD Code for landline numbers'),
        ),
    ]
