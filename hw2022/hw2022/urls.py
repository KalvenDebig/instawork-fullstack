"""hw2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path
from django.views import static as sc
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from api.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add),
    path('edit/', edit),
    path('add_page/', add_page),
    path('edit_page/', edit_page),
    path('delinfo/', delinfo),
    path('infoshow/', infoshow),
    path('', infoshow),
    re_path(r'^static/(?P<path>.*)$', sc.serve, {'document_root': os.path.join(BASE_DIR, 'static')})

]
