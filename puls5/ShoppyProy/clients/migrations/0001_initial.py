# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
