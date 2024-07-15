from django import forms
# Вызываем готовый модель для Пользователя
from django.contrib.auth.models import User
# Вызываем готовый модуль для создании пользователя
from django.contrib.auth.forms import UserCreationForm

# Форма для регистрации
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'password1', 'password2']

# Форма для логина
class UserLoginForm(forms.Form):
    username = forms.CharField() # ADMin
    password = forms.CharField(widget=forms.PasswordInput)  #asdin3f0