from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from .forms import AnketaForm
from datetime import datetime
from .models import Post



# Create your views here.
# TODO:  make this


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

    paginate_by = 1







# def registration(request):
#     # Renders the registration page.
#     assert isinstance(request, HttpRequest)
#     if request.method == "POST":  # после отправки формы
#         regform = UserCreationForm(request.POST)
#         if regform.is_valid():  # валидация полей формы
#             reg_f = regform.save(commit=False)  # не сохраняем автоматически данные формы
#             reg_f.is_staff = False  # запрещен вход в административный раздел
#             reg_f.is_active = True  # активный пользователь
#             reg_f.is_superuser = False  # не является суперпользователем
#             reg_f.date_joined = datetime.now()  # дата регистрации
#             reg_f.last_login = datetime.now()  # дата последней авторизации
#             reg_f.save()  # сохраняем изменения после добавления данных
#             return redirect('app:home')  # переадресация на главную страницу после регистрации
#     else:
#         regform = UserCreationForm()  # создание объекта формы для ввода данных нового пользователя
#         return render(request, 'registration.html', {'regform': regform, 'year': datetime.now().year, })


def anketa(request):
    assert isinstance(request, HttpRequest)
    form = AnketaForm(request.POST or None)
    instance=None
    if request.method == "POST":
        if form.is_valid():
            #instance = form.save(commit=False)
            #instance.save()
            form = None
    else:
        form=AnketaForm()
    return render(request,'anketa.html',{'form':form})
