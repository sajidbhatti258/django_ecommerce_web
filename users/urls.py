# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from .views import UserRegisterView, UserLoginView, UserProfileDetailView, UserProfileUpdateView

app_name = 'users'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', UserProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
]
