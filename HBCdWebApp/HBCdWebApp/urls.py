"""
URL configuration for HBCdWebApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# noinspection PyUnresolvedReferences
from django.urls import path, include
from prayer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prayer/', views.home, name='home'),
    path('prayer/home', views.home, name='home'),
    path('', views.home, name='home'),
    path('auth/',include('users.urls')),
]
