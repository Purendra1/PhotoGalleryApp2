from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=(("M", "M"),("F", "F"),("T", "T"))))
    image = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','firstname','lastname','gender','image']

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already in use.')




class ProfileUpateForm(forms.ModelForm):
	
	class Meta:
		model=Profile
		fields=['image','gender','firstname','lastname','email']



class AlbumCreationForm(forms.ModelForm):
	class Meta:
		model=Album
		fields=['title','description','cover']




class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields = ['description','image','albumid']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(PhotoForm, self).__init__(*args, **kwargs)
       self.fields['albumid'].queryset = Album.objects.filter(owner=user)





class PhotoFormInAlbum(forms.ModelForm):
    class Meta:
        model=Photo
        fields = ['description','image','albumid']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        key = kwargs.pop('albumid')
        super(PhotoFormInAlbum, self).__init__(*args, **kwargs)
        self.fields['albumid'].queryset = Album.objects.filter(albumid=key)


class PhotoFormInAlbumAPI(forms.ModelForm):
    class Meta:
        model=Photo
        fields = ['description','image','albumid']

    def __init__(self, *args, **kwargs):
        try:
            kwa=kwargs.pop('kwargs')
            user = kwa.pop('user')
            key = kwa.pop('albumid')
            super(PhotoFormInAlbumAPI, self).__init__(*args, **kwargs)
            self.fields['albumid'].queryset = Album.objects.filter(albumid=key)
        except:
            pass