from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from .forms import AnketaForm, CommentForm
from datetime import datetime
from .models import Articles
from django.urls import reverse_lazy


# Create your views here.
# TODO:  make this


class BlogListView(ListView):
    model = Articles
    template_name = 'home.html'

    paginate_by = 1



class BlogDetailView(FormMixin,DetailView):
    model = Articles
    template_name = 'post_detail.html'
    form_class = CommentForm
    context_object_name = 'get_post'

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('app:post_detail', kwargs={'pk':self.get_object().id})

    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.comment_article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class BlogCreateView(CreateView):
    model=Articles
    template_name = 'post_create.html'
    fields=['title','body','status']
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


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
