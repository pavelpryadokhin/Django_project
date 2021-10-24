from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



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

class ProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        del self.fields['password']
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username':'Логин',
        }