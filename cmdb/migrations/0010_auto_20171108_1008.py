# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-08 02:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0009_auto_20171107_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sl',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Service_Line',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
