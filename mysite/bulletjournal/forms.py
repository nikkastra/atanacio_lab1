from django import forms
from .models import *

class FirstName(forms.Form):
    name = forms.CharField(label="Hello! What is your name? ", max_length=100)


class NicknameAndBio(forms.ModelForm):
	class Meta:
		model = Name
		fields = ['nickname', 'bio']


class Picture(forms.ModelForm):
	class Meta:
		model = Name
		fields = ['image']