from django.urls import path
from . import views
urlpatterns = [
   path('hani', views.index)
   path('hani/abd', views.hani)
]