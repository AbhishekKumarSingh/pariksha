# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_question_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(related_name='choices', to='quiz.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(related_name='questions', to='quiz.Quiz'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='user',
            field=models.ForeignKey(related_name='responses', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
