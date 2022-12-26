from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from accounts.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")


class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("email", "password")
