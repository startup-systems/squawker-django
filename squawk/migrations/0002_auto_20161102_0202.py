# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squawk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squawk',
            name='auto_increment_id',
        ),
        migrations.AddField(
            model_name='squawk',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
