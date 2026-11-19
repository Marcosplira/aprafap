from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('transparencia/', views.transparencia,
         name='transparencia'),
]