# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-26 07:12
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
