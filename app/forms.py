from django import forms
from .models import  Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['comment_text']

class AnketaForm(forms.Form):
    name = forms.CharField(label='Name', min_length=2, max_length=100)
    city = forms.CharField(label='city', min_length=2, max_length=100)
    job = forms.CharField(label='job', min_length=2, max_length=100)
    gender = forms.ChoiceField(label="gender",
                               choices=[('1', 'male'), ('2', 'female')],
                               widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Вы пользуетесь интернетом',
                                 choices=(('1', 'Каждый день'),
                                          ('2', 'Несколько раз в день'),
                                          ('3', 'Несколько раз неделю'),
                                          ('4', 'Несколько раз в месяц')), initial=1)
    notice = forms.BooleanField(label='Получать новости?',
                                required=False)
    email=forms.EmailField(label='e-mail', min_length=7)
    message=forms.CharField(label='Коротко о себе',
                            widget=forms.Textarea(attrs={'rows':12,'cols':20}))

