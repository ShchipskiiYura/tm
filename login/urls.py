from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.login.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("home/", views.home, name="home"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('google/', views.GoogleLogin.as_view(), name='google_login'),
    path('facebook/', views.FacebookLogin.as_view(), name='facebook_login'),
    path('github/', views.GithubLogin.as_view(), name='github_login'),
]