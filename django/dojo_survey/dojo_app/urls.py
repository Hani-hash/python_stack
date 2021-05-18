from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('info', views.index),
    path('rand', views.trial),
    
]