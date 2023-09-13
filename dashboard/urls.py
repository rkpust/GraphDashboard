from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration),
    path('registration/', views.registration, name='registration'),
    path('dashboard/', views.index, name='dashboard-index'),
]