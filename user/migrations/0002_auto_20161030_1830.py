# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concreteuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Usuário com esse email já existe.'}, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='concreteuser',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]