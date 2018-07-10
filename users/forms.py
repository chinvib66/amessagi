from django import forms
from django.contrib.auth.models import User
from .models import a_M_user
from django.utils.translation import gettext_lazy as _



class aMForm(forms.ModelForm):
    
    class Meta:
        model = a_M_user
        exclude = ['user']
        
    
class UserRegForm(forms.Form):
    first_name = forms.CharField(max_length = 255)
    last_name = forms.CharField(max_length = 255)
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.EmailField(
        label = 'Email'
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password' ]