from django.contrib import admin
from django.urls import path
from . import views
from .views import Profiles

urlpatterns = [
    path('usersprofile/', views.profiles, name='profile'),
    # path('usersprofile/', Profiles.as_view(), name='profile'),
]
