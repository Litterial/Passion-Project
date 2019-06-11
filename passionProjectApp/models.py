from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
import datetime
# Create your models here.
# class Question(models.Model):
#     title=models.CharField(max_length=1000)
#     question=models.CharField(max_length=1000)
#
#     def __str__(self):
#         return self.title

class RealQuestion(models.Model):
    title = tinymce_models.HTMLField()
    question = tinymce_models.HTMLField()
    last_update=models.DateTimeField(default=datetime.datetime.utcnow())
    date_created=models.DateTimeField(default=datetime.datetime.utcnow())
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class RealQuestionComment(models.Model):
    message= tinymce_models.HTMLField()
    last_update=models.DateTimeField(default=datetime.datetime.utcnow())
    date_created=models.DateTimeField(default=datetime.datetime.utcnow())
    parent=models.ForeignKey(RealQuestion,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

class Answer(models.Model):
    message= tinymce_models.HTMLField()
    last_update=models.DateTimeField(default=datetime.datetime.utcnow())
    date_created=models.DateTimeField(default=datetime.datetime.utcnow())
    parent=models.ForeignKey(RealQuestion,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

class AnswerComment(models.Model):
    message= tinymce_models.HTMLField()
    last_update=models.DateTimeField(default=datetime.datetime.now())
    date_created=models.DateTimeField(default=datetime.datetime.now())
    parent=models.ForeignKey(Answer,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.message


