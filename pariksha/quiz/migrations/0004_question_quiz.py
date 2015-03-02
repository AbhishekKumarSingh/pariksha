# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20150223_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default=1, to='quiz.Quiz'),
            preserve_default=False,
        ),
    ]
