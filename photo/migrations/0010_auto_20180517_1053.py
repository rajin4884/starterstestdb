# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0009_auto_20180517_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_re_level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='b_re_step',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='b_ref',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
