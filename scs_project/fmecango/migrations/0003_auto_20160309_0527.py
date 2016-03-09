# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('fmecango', '0002_table_diagram'),
    ]

    operations = [
        migrations.AddField(
            model_name='failuremode',
            name='risk',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='failuremode',
            name='detection',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='failuremode',
            name='notes',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='failuremode',
            name='occurence',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='failuremode',
            name='severity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
