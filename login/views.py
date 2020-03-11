from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


class login(View):
  def get(self, request):
    return render(request, 'login.html')

@login_required
def home(request):
  return render(request, 'home.html')

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    # callback_url = CALLBACK_URL_YOU_SET_ON_GITHUB
    client_class = OAuth2Client

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter