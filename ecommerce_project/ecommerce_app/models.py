from django.db import models

# Create your models here.
# ecommerce_app/models.py
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def _str_(self):
        return self.name

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")

    def _str_(self):
        return f"Order #{self.id} - {self.customer.name}"