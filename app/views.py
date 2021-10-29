from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .forms import  CommentForm
from datetime import datetime
from .models import Articles, Vote
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
# TODO:  make this


class BlogListView(ListView):
    model = Articles
    template_name = 'home.html'

    paginate_by = 4



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
    fields=['title','body','status','image']
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model=Articles
    template_name = 'post_update.html'
    fields=['title','body','status','image']

class BloqDeleteView(DeleteView):
    model=Articles
    template_name = 'post_delete.html'
    success_url = reverse_lazy('app:home')

@login_required  # только аутентифицированные пользователи могут голосовать
def vote(request, pk, reaction):
    article = get_object_or_404(Articles, pk=pk)
    vote, created = Vote.objects.get_or_create(voter=request.user, article=article,
                                         defaults={'positive': reaction})
    if not created:
        messages.warning(request,"Голосовать можно один раз")
    next = request.META.get('HTTP_REFERER', article)
    return redirect(next)

