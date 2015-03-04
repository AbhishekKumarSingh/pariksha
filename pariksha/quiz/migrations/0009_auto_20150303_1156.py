# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20150303_1012'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userresponse',
            unique_together=set([('user', 'question')]),
        ),
    ]
