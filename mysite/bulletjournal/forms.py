from django import forms
from .models import *

class FirstName(forms.Form):
    name = forms.CharField(label="Hello! What is your name? ", max_length=100)


class Nickname(forms.Form):
	nickname = forms.CharField(label="", max_length=100, required=False)


class Bio(forms.Form):
	bio = forms.CharField(label='', max_length=100, required=False)


class Picture(forms.ModelForm):
	class Meta:
		model = Name
		fields = ['image']


class Keys(forms.ModelForm):
	class Meta:
		model = Key
		fields = ['key', 'description']