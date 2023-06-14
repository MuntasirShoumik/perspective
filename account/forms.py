from django import forms
from .models import Account
from django.core.validators import *
import re

class RegistrationForm(forms.ModelForm):

    class Meta:
        model=Account
        fields = "__all__"


    def name_check(name):
        if ' ' in name:
            raise forms.ValidationError("Name can not contain white space!")
        if bool(re.search(r'\d', name)):
            raise forms.ValidationError("Name can not contain any number!")

    def uname_check(uname):
        if Account.objects.filter(user_name = uname).exists():
            raise forms.ValidationError("user name has already taken!")
        

    def email_check(val):
        if Account.objects.filter(email = val).exists():
            raise forms.ValidationError("an account with this email already exist please login!")
        

    def pass_check(val):
        if not bool(re.search(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', val)):
            raise forms.ValidationError("minimum 8 characters in length, At least one uppercase English letter, At least one lowercase English letter, At least one digit, At least one special character!")
         

    first_name = forms.CharField(max_length=20, validators=[name_check],label="First name")
    last_name = forms.CharField(max_length=20,validators=[name_check],label="Last name")
    user_name = forms.CharField(max_length=20,label="User name",validators=[uname_check])
    email = forms.EmailField(validators=[EmailValidator,email_check], label="Email")
    profile_image = forms.ImageField(label="Upload Profile",required=False)
    password = forms.CharField(validators=[pass_check],label="Password")


def if_exist(uname,password):
    if not Account.objects.filter(user_name = uname,password = password).exists():
        raise forms.ValidationError("Wrong User Name Or Password")


class LoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField()
    
