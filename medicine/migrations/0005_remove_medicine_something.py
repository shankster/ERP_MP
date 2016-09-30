# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0004_auto_20160929_0409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='something',
        ),
    ]
