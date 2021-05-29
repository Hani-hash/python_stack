from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.root),
    path('register', views.register),
    path('success', views.success),

    path('logout', views.logout),
    path('login', views.login)
]

