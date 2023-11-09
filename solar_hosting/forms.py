from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, HostingPlan
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import ContactMessage


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
    fields = ['password1', 'password2']


class HostingPurchaseForm(forms.Form):
    plan = forms.ModelChoiceField(queryset=HostingPlan.objects.all(), empty_label=None, label="Select Hosting Plan")


class DomainPurchaseForm(forms.Form):
    domain_name = forms.CharField(max_length=255, label="Enter domain name")


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'comments']
