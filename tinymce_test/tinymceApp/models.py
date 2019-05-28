from django.db import models

# Create your models here.

from django.db import models
# from tinymce_test import models as tinymce_models

class MyModel(models.Model):
    my_field = tinymce_models.HTMLField()

class test(models.Model):
    title=models.CharField()