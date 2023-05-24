# recipes/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name="animais-inicio"),
]
