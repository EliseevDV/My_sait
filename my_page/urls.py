"""
URL configuration for my_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include
from horoscope import views
from horoscope.views import index

urlpatterns = [

    path('', index, name='start_page'),
    path('admin/', admin.site.urls),
    path('beautiful_table/', views.beautiful_table, name='beautiful_table'),
    path('horoscope/', include('horoscope.urls')),
    path('todo_week/', include('week_days.urls')),
    path('calculate_geometry/', include('geometry.urls')),

]
