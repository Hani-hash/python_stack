from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy),
    path('destroy', views.destroy),
    path('addtwo', views.addtwo),
    path('addnum', views.increment),
    
]