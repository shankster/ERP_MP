# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20160929_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='contact_number',
            field=models.CharField(max_length=10, default='None', help_text='Enter STD Code for landline numbers'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email_id',
            field=models.EmailField(max_length=254, help_text='Enter Valid Email ID'),
        ),
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
