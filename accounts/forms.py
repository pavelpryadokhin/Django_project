from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Имя',max_length=30, required=False, help_text='Введите ваше имя')
    last_name = forms.CharField(label='Фамилия',max_length=30, required=False, help_text='Введите вашу фамилию')
    email = forms.EmailField(max_length=254, help_text='Введите адрес вашей почты')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'username':'Логин',
        }