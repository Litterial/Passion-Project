from django.contrib import admin
from .models import MyModel,test
# Register your models here.
admin.site.register(MyModel)
admin.site.register(test)