from django.urls import path
from . import views

urlpatterns = [
    path('solar_hosting/', views.index, name="main"),
]