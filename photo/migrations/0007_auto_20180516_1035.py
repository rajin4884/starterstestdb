# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-16 01:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_auto_20180516_0048'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mrapply_State',
        ),
        migrations.RemoveField(
            model_name='board',
            name='b_categ_num',
        ),
        migrations.AlterField(
            model_name='review',
            name='mrapply_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.Mrapply'),
        ),
    ]