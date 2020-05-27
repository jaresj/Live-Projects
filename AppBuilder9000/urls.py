"""AppBuilder9000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('ed/', include('EdsApp.urls')),
    path('footy/', include('FootyApp.urls')),
    path('laapp/', include('LAApp.urls')),
    path('foody/', include('FoodyApp.urls')),
    path('hiking/', include('HikingApp.urls')),
    path('shoecloset/', include('ShoeCloset.urls')),
    path('modify/', include('Modify.urls')),
    path('texasscore/', include('TexasScore.urls')),
    path('fittrack/', include('FitTrack.urls')),
    path('GreatestComedies/', include('GreatestComedies.urls')),
    path('game/', include('GameApp.urls')),
]

