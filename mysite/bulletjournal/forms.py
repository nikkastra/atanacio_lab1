from django import forms

class IndexCardForm(forms.Form):
    name = forms.CharField(label="Hello! What is your name? ", max_length=100)