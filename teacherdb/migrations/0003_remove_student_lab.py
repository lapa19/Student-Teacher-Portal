# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 18:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacherdb', '0002_auto_20170114_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='lab',
        ),
    ]
