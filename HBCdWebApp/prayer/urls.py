# pages/urls.py

from django.urls import path
from prayer import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home1'),
    path('', views.home, name='home2'),
]
