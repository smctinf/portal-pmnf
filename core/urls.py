

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('2/', views.index2, name='index2'),
]
