
from django.urls import path, include
from . import views

urlpatterns = [
    #Function base view
    path('about_me/', views.about_me),
    path('', views.landing),
]
