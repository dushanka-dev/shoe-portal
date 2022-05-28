from django.contrib import admin
from django.urls import path
from . import views
from .views import CheckoutForm, CheckoutSuccess
from .webhooks import webhook

urlpatterns = [
    path('', CheckoutForm.as_view(), name='checkout'),
    path('checkout-success/<order_number>', CheckoutSuccess.as_view(), name='checkout_success'),
    path('wh/', webhook, name='webhook'),
]
