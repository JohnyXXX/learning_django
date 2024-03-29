from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Board


class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'photo', 'content', 'price', 'rubric')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
