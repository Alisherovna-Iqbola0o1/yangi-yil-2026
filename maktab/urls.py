from django.urls import path
from . import views

urlpatterns = [
    path('', views.maktab_list, name='maktab_list'),
    path('direktorlar/', views.direktor_list, name='direktor_list'),
]
