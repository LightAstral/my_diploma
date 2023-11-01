from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, HostingPlan, TestimonialComment
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'required': 'required'}),
            'last_name': forms.TextInput(attrs={'required': 'required'}),
        }


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')


class NameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class EmailChangeForm(forms.Form):
    email = forms.EmailField()


class PhoneChangeForm(forms.Form):
    phone = forms.CharField(max_length=15)


class PasswordChangeForm(PasswordChangeForm):
    pass


class HostingPurchaseForm(forms.Form):
    plan = forms.ModelChoiceField(queryset=HostingPlan.objects.all(), empty_label=None, label="Select Hosting Plan")


class TestimonialCommentForm(forms.ModelForm):
    class Meta:
        model = TestimonialComment
        fields = ['text']  # Укажите поля, которые пользователь может заполнить