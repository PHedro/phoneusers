# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddd', models.CharField(max_length=3, verbose_name='DDD')),
                ('number', models.CharField(max_length=9, verbose_name='Número')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]