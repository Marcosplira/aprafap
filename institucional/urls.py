from django.urls import path
from . import views

urlpatterns = [
    path('transparencia/', views.transparencia,
         name='transparencia'),
]