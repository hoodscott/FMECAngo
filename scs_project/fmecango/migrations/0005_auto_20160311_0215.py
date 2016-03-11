# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('fmecango', '0004_auto_20160310_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failuremode',
            name='detection',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='failuremode',
            name='occurence',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='failuremode',
            name='severity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
