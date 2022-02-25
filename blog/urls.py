from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #Function base view
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]
