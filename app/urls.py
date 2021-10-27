from django.contrib import admin
from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/create/', views.BlogCreateView.as_view(),name='post_create'),
    path('', views.BlogListView.as_view(), name='home'),
]