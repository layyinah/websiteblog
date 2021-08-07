from.models import Blog
from django import forms
class Todoforms(forms.ModelForm):
    class Meta:
        model= Blog
        fields=['name','desc','img','date']
