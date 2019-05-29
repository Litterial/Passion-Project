from django.contrib import admin
from .models import RealQuestion,RealQuestionComment,Answer,AnswerComment
# Register your models here.

admin.site.register(RealQuestion)
admin.site.register(RealQuestionComment)
admin.site.register(Answer)
admin.site.register(AnswerComment)
