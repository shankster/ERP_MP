# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0006_auto_20160929_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=100000, primary_key=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='serial_no',
            field=models.AutoField(max_length=100000, primary_key=True, serialize=False),
        ),
    ]
