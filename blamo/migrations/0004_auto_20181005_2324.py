# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-05 23:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blamo', '0003_blamohost_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blamohost',
            old_name='host',
            new_name='hostname',
        ),
    ]