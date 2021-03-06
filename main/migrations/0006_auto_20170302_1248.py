# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-02 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170302_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.FileField(upload_to='img/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='good',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
