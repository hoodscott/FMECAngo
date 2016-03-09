# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmecango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='diagram',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
