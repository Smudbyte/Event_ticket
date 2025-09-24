from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User  # your custom user model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
