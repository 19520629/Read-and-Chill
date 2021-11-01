from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from . import views
urlpatterns = [
    path('home', views.home, name='home'),
]
