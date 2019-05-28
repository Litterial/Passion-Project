from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=1000)
    question=models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class RealQuestion(models.Model):
    title = tinymce_models.HTMLField()
    question = tinymce_models.HTMLField()

    def __str__(self):
        return self.title

