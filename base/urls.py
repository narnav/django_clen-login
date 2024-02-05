from django.contrib import admin
from django.urls import path

from base import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', views.index),
    path('login/', TokenObtainPairView.as_view()),
    path('secret/', views.secret),
    
]
