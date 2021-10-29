from django.urls import path
from accounts import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
app_name='accounts'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('passworld_change/', PasswordChangeView.as_view(), name='password_change'),
    path('passworld_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

]