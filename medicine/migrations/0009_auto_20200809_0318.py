# Generated by Django 3.1 on 2020-08-08 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0008_auto_20160929_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='serial_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
