from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View, generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from blogapp.models import ArticlePost
# Create your views here.

class home(generic.ListView):
    template_name = 'pages/home.html'
    model = ArticlePost


class article(generic.DetailView):
    #model = ArticlePost
    template_name = 'pages/article.html'
    queryset = ArticlePost.objects.all()
    

