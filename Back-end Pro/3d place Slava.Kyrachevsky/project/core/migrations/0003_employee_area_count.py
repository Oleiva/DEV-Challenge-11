# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_employee_is_busy'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='area_count',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]