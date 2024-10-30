from django.test import TestCase
from django.urls import path
from . import views

# Create your tests here.
urlpatterns = [
    path('home', views.valores_api.as_view(), name='home')
]