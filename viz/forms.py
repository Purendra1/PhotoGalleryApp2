from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' , 'firstname' , 'lastname']

class ProfileUpateForm(forms.ModelForm):
	
	class Meta:
		model=Profile
		fields=['image','gender']
