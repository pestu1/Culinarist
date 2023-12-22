"""määrittelee url patternit käyttäjille"""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #rekisteröinti sivu
    path('register/', views.register, name='register'),


]
