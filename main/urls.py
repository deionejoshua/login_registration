from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('user_login', views.login_page),
    path('process_login', views.process_login),
    path('dashboard', views.dashboard),
    path('logout', views.logout)
]