from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_dojo', views.add_dojo),
    path('insert_ninja', views.insert_ninja)
]
