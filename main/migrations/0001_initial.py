# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-31 20:22
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='squawk',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('post', models.CharField(max_length=140)),
                ('timestamp', models.FloatField()),
            ],
        ),
        
    ]