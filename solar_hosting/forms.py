# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import User
#
#
# class CustomUserCreationForm(UserCreationForm):
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'phone', 'password1', 'password2')
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')
