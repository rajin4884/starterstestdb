# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-16 01:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0007_auto_20180516_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='mtr_lesson',
            new_name='state_name',
        ),
    ]
