from django import forms

#로그인 폼
class NameForm(forms.Form):
    idenetifier = forms.CharField(label='ID', max_length=100,required=True)
    secret=forms.CharField(label='PASSWORD',max_length=100,required=True)
#회원가입 폼
class RegiForm(forms.Form):
    first_name=forms.CharField(label='first name', max_length=100,required=True)
    last_name=forms.CharField(label='last name', max_length=100,required=True)
    email=forms.EmailField(label='email', max_length=100,required=True)
    idenetifier = forms.CharField(label='ID', max_length=100,required=True)
    secret=forms.CharField(label='PASSWORD',max_length=100,required=True)

