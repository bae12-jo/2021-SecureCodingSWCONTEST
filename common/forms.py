from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
   class Meta:
        model = User
        fields = ('username','email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
