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
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')


class EmailChangeForm(forms.Form):
    email = forms.EmailField()


class PhoneChangeForm(forms.Form):
    phone = forms.CharField(max_length=15)


class PasswordChangeForm(PasswordChangeForm):
    pass