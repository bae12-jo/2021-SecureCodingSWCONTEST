
from django import forms

class NameForm(forms.Form):
    idenetifier = forms.CharField(label='ID', max_length=100)
    secret=forms.CharField(label='PASSWORD',max_length=100)

class RegiForm(forms.Form):
    idenetifier = forms.CharField(label='ID', max_length=100)
    secret=forms.CharField(label='PASSWORD',max_length=100)
