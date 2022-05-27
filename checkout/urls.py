from django.contrib import admin
from django.urls import path
from . import views
from .views import CheckoutForm

urlpatterns = [
    path('', CheckoutForm.as_view(), name='checkout'),
]