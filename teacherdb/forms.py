from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import Student

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class Regno(forms.Form):
	regno = forms.ModelChoiceField(label = "Select Registration No.:",widget=forms.Select(attrs={'class': 'form-control','style':'width:110px','name':'regno'}),queryset=Student.objects.values_list('regno', flat=True))
