from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
import datetime
from django.utils import timezone
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
    last_update=models.DateTimeField(default=timezone.now)
    date_created=models.DateTimeField(default=timezone.now)
    upvote=models.ManyToManyField(User,blank=True,related_name='question_upvotes')
    downvote=models.ManyToManyField(User,blank=True,related_name='question_downvotes')
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class RealQuestionComment(models.Model):
    message= tinymce_models.HTMLField()
    last_update=models.DateTimeField(default=timezone.now)
    date_created=models.DateTimeField(default=timezone.now)
    parent=models.ForeignKey(RealQuestion,on_delete=models.CASCADE)
    upvote=models.ManyToManyField(User,blank=True,related_name='questcom_upvotes')
    downvote=models.ManyToManyField(User,blank=True,related_name='questcom_downvotes')
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

class Answer(models.Model):
    message= tinymce_models.HTMLField()
    last_update=models.DateTimeField(default=timezone.now)
    date_created=models.DateTimeField(default=timezone.now)
    parent=models.ForeignKey(RealQuestion,on_delete=models.CASCADE)
    upvote=models.ManyToManyField(User,blank=True,related_name='answer_upvotes')
    downvote=models.ManyToManyField(User,blank=True,related_name='answer_downvotes')
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

class AnswerComment(models.Model):
    message= tinymce_models.HTMLField()
    last_update=models.DateTimeField(default=timezone.now)
    date_created=models.DateTimeField(default=timezone.now)
    parent=models.ForeignKey(Answer,on_delete=models.CASCADE)
    upvote=models.ManyToManyField(User,blank=True,related_name='anscom_upvotes')
    downvote=models.ManyToManyField(User,blank=True,related_name='anscom_downvotes')
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.message


