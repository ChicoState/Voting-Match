# Documentation about Django forms: 
# https://docs.djangoproject.com/en/4.1/topics/forms/
#
# Form fields:
# https://docs.djangoproject.com/en/4.1/ref/forms/fields/

from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Voter

class RegisterForm(UserCreationForm):
    class Meta:
        model = Voter
        fields = ["username", "password1", "password2"]