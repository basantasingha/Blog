# myapp/forms.py
from django import forms
from .models import ImageModel, Category, AuthModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['name', 'image','category', 'content']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

class AuthForm(forms.ModelForm):
    model = AuthModel
    fields = ['username','password']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Passwords do not match')
        return password_confirm