from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('dashboard/', views.index, name='dashboard-index'),
]