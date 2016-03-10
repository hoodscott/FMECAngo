# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmecango', '0003_auto_20160309_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='diagram',
            field=models.ImageField(null=True, upload_to=b'diagrams/%Y/%m/%d/', blank=True),
        ),
    ]
