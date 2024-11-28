from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)  # Customer's full name
    email = models.EmailField(unique=True)  # Email must be unique for each customer

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    # ForeignKey establishes a one-to-many relationship with Customer.
    # on_delete=models.CASCADE ensures that if a Customer is deleted, all associated orders are deleted.

    order_date = models.DateTimeField(auto_now_add=True)  # Automatically set to the current datetime when created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount of the order

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
