from django.contrib import admin
from django.urls import path, include
from .views import invitation_guest

urlpatterns = [
    path('<str:slug>/', invitation_guest, name='name'),
]
