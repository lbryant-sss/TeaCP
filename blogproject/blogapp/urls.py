from django.conf import settings
from blogapp import views
from django.contrib import admin
from django.urls import path, include
from blogapp.views import *

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('<slug:slug>/', article.as_view(), name='article'),
]