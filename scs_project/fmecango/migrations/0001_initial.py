# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('function', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='FailureMode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('cause', models.CharField(max_length=128)),
                ('effect', models.CharField(max_length=128)),
                ('severity', models.IntegerField()),
                ('occurence', models.IntegerField()),
                ('detection', models.IntegerField()),
                ('notes', models.CharField(max_length=128)),
                ('component', models.ForeignKey(to='fmecango.Component')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='table',
            field=models.ForeignKey(to='fmecango.Table'),
        ),
    ]
