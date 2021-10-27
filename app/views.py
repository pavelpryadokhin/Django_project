from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
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
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('app:home')
    else:
        form=AnketaForm()
    return render(request,'anketa.html',{'form':form})

# def like_or_dislike(request, post_id, is_like):
#     try:
#         post = Articles.objects.get(id = post_id)
#     except:
#         raise Http404("Пост не найден!")
#     old_like = Like.objects.filter(user = request.user, for_post = post)
#     if old_like:
#         like = Like.objects.get(user = request.user, for_post = post)
#         if like.like_or_dislike == 'like' and is_like == 'like':
#             like.delete()
#             post.post_like -= 1
#             post.save()
#         elif like.like_or_dislike == 'dislike' and is_like == 'dislike':
#             like.delete()
#             post.post_dislike -= 1
#             post.save()
#         elif like.like_or_dislike == 'like' and is_like == 'dislike':
#             like.like_or_dislike = 'dislike'
#             like.save()
#             post.post_dislike += 1
#             post.post_like -= 1
#             post.save()
#         elif like.like_or_dislike == 'dislike' and is_like == 'like':
#             like.like_or_dislike = "like"
#             like.save()
#             post.post_dislike -= 1
#             post.post_like += 1
#             post.save()
#     else:
#         new_like = Like(user = request.user, for_post = post, like_or_dislike = is_like)
#         new_like.save()
#         if is_like == 'like':
#             post.post_like += 1
#             post.save()
#         elif is_like == 'dislike':
#             post.post_dislike += 1
#             post.save()
#
#     is_like = Like.objects.filter(user = request.user, for_post = post)
#     if is_like:
#         user_like = True
#         is_like = Like.objects.get(user = request.user, for_post = post)
#         user_like_val = is_like.like_or_dislike
#     else:
#         user_like = False
#         user_like_val = ''
#
#     content={
#                 "result": True,
#                 "user_like": user_like,
#                 "user_like_val": user_like_val,
#                 "like": post.post_like,
#                 "dislike": post.post_dislike
#             }
#     return HttpResponse(
#         json.dumps({
#             "result": True,
#             "user_like": user_like,
#             "user_like_val": user_like_val,
#             "like": post.post_like,
#             "dislike": post.post_dislike
#         }),
#         content_type="application/json"
#     )