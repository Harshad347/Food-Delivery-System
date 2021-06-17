from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomerRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomerRegisterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RestaurantRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RestaurantRegisterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label='username', widget=forms.TextInput(
        attrs={'class': 'form__input', 'placeholder': 'Harshad347'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form__input', 'placeholder': '••••••••••'}))

    class Meta:
        model = User
        fields = ['username', 'password']
