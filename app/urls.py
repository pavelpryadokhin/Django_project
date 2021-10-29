from django.contrib import admin
from django.urls import path, re_path
from app import views

app_name = 'app'

urlpatterns = [
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/create/', views.BlogCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/update/', views.BlogUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete/', views.BloqDeleteView.as_view(),name='post_delete'),
    re_path(r'^vote/(?P<pk>\d+)/(?P<reaction>True|False)/$', views.vote, name='vote'),
    path('', views.BlogListView.as_view(), name='home'),
]