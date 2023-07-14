from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import tbBooking
from django.views.generic import ListView
from django.core.validators import MinValueValidator


class UserSignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
            }
        )
    )
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control',
            }
        )
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control',
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'data-toggle': 'password',
                'id': 'password',
            }
        )
    )
    password2 = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'class': 'form-control',
                'data-toggle': 'password',
                'id': 'password',
            }
        )
    )


class DateTimeLocalInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    

class BookingForm(forms.Form):
    date = forms.DateTimeField(
        required=True,
        input_formats=['%Y-%m-%d %H:%M'],
        widget=DateTimeLocalInput(attrs={'class': 'form-control'})
    )

    guests = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Guests'}),
        validators=[MinValueValidator(1)]
    )