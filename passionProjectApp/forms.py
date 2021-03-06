from django import forms
from .models import RealQuestion,Answer,RealQuestionComment,AnswerComment
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE

class RealQuestionForm(forms.ModelForm):
    title=forms.CharField(widget=TinyMCE(mce_attrs={'height':'100px'}))
    class Meta:
        model = RealQuestion
        fields=['title','question','topic']

        widgets={'topic':forms.TextInput(attrs={'placeholder':'(e.g algebra,calculus)'})}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields=['message']

class CommentQuestionForm(forms.ModelForm):
    class Meta:
        model = RealQuestionComment
        fields=['message']
class CommentAnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerComment
        fields=['message']



class UserForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        userData=self.cleaned_data['username']
        print(userData)
        if User.objects.filter(username=userData).exists():
            print("error")
            raise forms.ValidationError("This user already exist")
        return userData

