# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=5)),
                ('open', models.CharField(max_length=5)),
                ('close', models.CharField(max_length=5)),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
