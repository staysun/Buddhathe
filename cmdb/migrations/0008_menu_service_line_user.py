# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-07 06:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0007_host_os_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
                ('url', models.CharField(blank=True, default=0, max_length=128, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pid', to='cmdb.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Service_Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_line_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('sl', models.ManyToManyField(null=True, to='cmdb.Service_Line')),
            ],
        ),
    ]