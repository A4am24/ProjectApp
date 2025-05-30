from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Hotel

class DisplayHotels(forms.ModelForm):
    class Meta:
        model=Hotel
        fields=['hotel_id', 'hotel_name', 'hotel_location', 'hotel_rating', 'price_per_night']

# Create Forms for Create Login

class Create(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(forms.ModelForm):
    email = forms.CharField(
        max_length = 150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password1'})
    )

