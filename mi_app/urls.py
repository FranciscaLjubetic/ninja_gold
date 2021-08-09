from django.urls import path
from . import views


urlpatterns = [
    path('', views.root),
    path('dos/', views.func2),
    path('tres/',views.saludaralvaro),
    path('blogs/new/', views.new),
    path('blogs/', views.index),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit/', views.edit),
    path('blogs/<int:number>/delete/', views.destroy),
    path('blogs/js/', views.json),
    path('home/<video>', views.home),
    path('entrar/<nombre>', views.entrar),
    path('salir/', views.salir),
    path('time/', views.time),
    path('login/', views.login),
]