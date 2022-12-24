from django import forms
from django.forms import ModelForm

from .models import *
#from .form import *

class TaskForm(forms.ModelForm):
    # title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    
    class Meta:
        model = TodoListItem
        fields = '__all__'