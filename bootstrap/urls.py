"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^grid_layout/$', grid_layout, name='grid_layout'),
    url(r'^toggle_button/$', toggle_button, name='toggle_button'),
    url(r'^modal/$', modal, name='modal'),
    url(r'^form/$', form, name='form'),
    url(r'^thumnail/$', thumnail, name='thumnail'),
    url(r'^jquery/$', jquery, name='jquery'),
]
