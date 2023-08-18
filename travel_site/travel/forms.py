from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)
    username = forms.CharField(label="Username", max_length=100)
    password1 = forms.CharField(
        label="Password", 
        max_length=100, 
        widget=forms.PasswordInput(attrs={'title': 'Password should be at least 8 characters long.'})
    )
    password2 = forms.CharField(
        label="Confirm Password", 
        max_length=100, 
        widget=forms.PasswordInput(attrs={'title': 'Please enter the same password as above.'})
    )


class AddTripForm(forms.Form):
    destination = forms.CharField(label="Destination", max_length=100)
    description = forms.CharField(label="Description", max_length=100)
    date_from = forms.DateField(label="Travel Date From")
    date_to = forms.DateField(label="Travel Date To")