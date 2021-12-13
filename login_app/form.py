from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from login_app.models import UserProfile

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=250)
    last_name=forms.CharField(max_length=250)
    email=forms.EmailField(label='Email Address', required=True)
    class Meta:
        model=User
        fields=('first_name','last_name','username','email', 'password1','password2')

class UserProfileChange(UserChangeForm):
    class Meta:
        model=User
        fields=('first_name', 'last_name', 'username', 'email', 'password')

class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic',]

