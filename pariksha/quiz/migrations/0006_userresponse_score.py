# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20150302_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresponse',
            name='score',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
