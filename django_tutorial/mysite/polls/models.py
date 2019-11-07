from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_lenth=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
