# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 01:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to=settings.AUTH_USER_MODEL),
        ),
    ]
