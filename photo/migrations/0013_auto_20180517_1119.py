# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0012_auto_20180517_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='b_num',
        ),
        migrations.AddField(
            model_name='board',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]