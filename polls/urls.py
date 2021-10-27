from django.contrib import admin
from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('<int:pk>/results/', views.ResultsView.as_view(),name='results'),
    path('<int:id>/', views.polldetail,name='detail'),
    # path('<int:id>/vote/', views.vote, name='vote'),
    path('', views.IndexView.as_view(),name='index'),
]
