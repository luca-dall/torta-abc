# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domande', '0005_annuncio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annuncio',
            old_name='risposta',
            new_name='stato',
        ),
    ]
