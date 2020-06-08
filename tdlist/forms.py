from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Business

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['title']
