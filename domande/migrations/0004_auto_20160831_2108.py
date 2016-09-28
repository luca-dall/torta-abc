# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 19:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domande', '0003_auto_20160822_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domanda',
            name='fetta',
            field=models.CharField(choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C')], max_length=1),
        ),
        migrations.AlterField(
            model_name='risposta',
            name='utente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]