# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quik_ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=200)),
                ('category', models.IntegerField()),
                ('ip', models.CharField(max_length=500)),
                ('count', models.IntegerField(default=1)),
            ],
        ),
    ]
