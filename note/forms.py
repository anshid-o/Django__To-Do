from django import forms
from django.forms import ModelForm

from .models import *

class NoteForm(forms.ModelForm):
    title=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new Note..'}))
    


    class Meta:
        model=Note
        fields='__all__'