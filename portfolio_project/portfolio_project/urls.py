"""
URL configuration for portfolio_project project.

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
from django.urls import path

from portfolio_project import views

urlpatterns = [
    path('',views.main_action, name='main'),
    path('contact',views.contact_action,name='contact'),
    path('class_projects', views.class_action,name='class'),
    path('IT_projects', views.it_action, name='it'),
    path('personal_projects',views.personal_action, name='personal'),
    path('cad_projects',views.cad_action, name='cad'),
]
