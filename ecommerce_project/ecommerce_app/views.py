from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Customer

def customer_orders(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.orders.all()
    return JsonResponse({
        "customer_name": customer.name,
        "orders": [{"id": order.id, "total_amount": order.total_amount} for order in orders]
    })

