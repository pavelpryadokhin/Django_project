from .forms import SignUpForm, ProfileForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('app:home')
    success_msg = 'Пользователь успешно создан'
    template_name = 'signup.html'
    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid


class ProfileView(generic.UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('app:home')
    template_name = 'profile.html'
