from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index),
    path('processmoney/<name>', views.processmoney),
    path('reset', views.reset),
    #path('config/<name>',views.config),
]