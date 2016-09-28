# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 19:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('domande', '0004_auto_20160831_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anno', models.IntegerField(choices=[(2016, 2016)], default=2016)),
                ('risposta', models.BooleanField(default=False)),
                ('utente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
