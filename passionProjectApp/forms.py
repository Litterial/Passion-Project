from django import forms
from .models import RealQuestion
from tinymce import models as tinymce_models
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

