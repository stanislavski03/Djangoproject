"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from app_lesson_4.views import view
from app_adv.views import *  #top_sellers, register



urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('app_adv.urls')),
    path('lesson_4', view),
    path('top-sellers/', top_sellers),
    path('register/', register),
    path('login/', login),
    path('advertisement/', advertisement),
    path('advertisement-post/', advertisement_post),
]


