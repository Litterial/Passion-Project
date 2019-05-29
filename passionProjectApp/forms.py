from django import forms
from .models import RealQuestion
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE

class RealQuestionForm(forms.ModelForm):
    ...
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    ...
    class Meta:
        model = RealQuestion
        fields='__all__'
        widgets={
            'title':TinyMCE(attrs={'height':'9000'}),

        }

class UserForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
    widgets={
        'password':forms.PasswordInput()

    }

    def clean(self):
        cleaned_data=super().clean()
        userData=cleaned_data.get('username')
        if User.objects.filter(userData).exists():
            raise forms.ValidationError("This user already exist")
        return cleaned_data