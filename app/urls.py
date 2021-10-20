from django.contrib import admin
from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    # path('registration/',views.registration, name='registration'),
    path('anketa/',views.anketa, name='anketa'),
    path('', views.BlogListView.as_view(), name='home'),
]