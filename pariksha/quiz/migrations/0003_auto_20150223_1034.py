# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0002_auto_20150217_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.ForeignKey(to='quiz.Choice')),
                ('question', models.ForeignKey(to='quiz.Question')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='score_point',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
