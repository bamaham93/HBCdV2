# pages/urls.py

from django.urls import path
from prayer import views

urlpatterns = [
    path("", views.home, name='home'),
]