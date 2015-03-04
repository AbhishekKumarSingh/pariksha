import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Quiz(models.Model):
    title = models.CharField(max_length=100, blank=False)
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User)
    user = models.ForeignKey(User, related_name='quizzes')

    def __unicode__(self):
        return self.title

    def maxPossibleScore(self):
        total = 0.0
        for question in self.questions_list.all():
            total = total + question.score_point
        return total

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    question_desc = models.TextField(blank=True)
    score_point = models.FloatField(default=0)
    author = models.ForeignKey(User)
    quiz = models.ForeignKey(Quiz, related_name='questions_list')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'




class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    isAnswer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class UserResponse(models.Model):
    user = models.ForeignKey(User, related_name='responses')
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Choice)
    score = models.FloatField(default=0)

    def __str__(self):
        return self.answer.choice_text

    class Meta:
        unique_together = ('user', 'question')
