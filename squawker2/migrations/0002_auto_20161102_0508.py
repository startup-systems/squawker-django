# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-02 05:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squawker2', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Squawks',
            new_name='postSquawks',
        ),
        migrations.RenameField(
            model_name='postsquawks',
            old_name='squawk',
            new_name='msg',
        ),
    ]
