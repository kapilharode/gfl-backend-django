# Generated by Django 3.1.6 on 2021-04-22 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GFL', '0002_auto_20210421_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.date, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date),
        ),
    ]
