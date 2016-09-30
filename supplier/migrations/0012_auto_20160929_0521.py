# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0011_auto_20160926_0324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_Name',
            new_name='supplier_name',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_ID',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
