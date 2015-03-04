# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20150303_0956'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userresponse',
            unique_together=set([('user', 'question', 'answer')]),
        ),
    ]
