from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class Password_Change_Form(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class:":"form-controle", 'placeholder':'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class:":"form-control", 'placeholder':'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class:":"form-controle", 'placeholder':'Confirm Password',}) )
    class meta:
        model = User
        fields =['old_password','new_password1','new_password2']