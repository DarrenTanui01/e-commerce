from django.urls import path
from .views import customer_orders

urlpatterns = [
    path('customer/<int:customer_id>/orders/', customer_orders),
]