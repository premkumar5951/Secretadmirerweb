from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import feedbackform


class formuser(UserCreationForm):
    username=forms.CharField(min_length=5,widget=forms.TextInput(attrs={'class':'form-control  my-2','placeholder':'username'}))
    first_name=forms.CharField(required=True , widget=forms.TextInput(attrs={'class':'form-control my-2 col-6','placeholder':'First name'}))
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Password'}))
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control  my-2','placeholder':'Re-type password'}))
    email=forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'email'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets={
        'last_name':forms.TextInput(attrs={'class':'form-control my-2 ','placeholder':'last name'})

        }

class feedform(forms.ModelForm):
    feedtxt=forms.CharField(max_length=500, required=True, min_length=15,widget=forms.Textarea(attrs={'class':'form-control my-2','placeholder':'Write your feedback here..',"rows":"5"}))
    email=forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'email'}))
    class Meta:
        model=feedbackform
        fields=['email','feedtxt']

    