from django.db import models
from django.utils.timezone import now  

class Member(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100, default="Staff")
    schedule = models.CharField(max_length=100, default="9AM-5PM")
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)
    join_date = models.DateField(default=now) 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Employee Info"
        verbose_name_plural = "Employee Info"

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Delivery(models.Model):
    delivery_id = models.CharField(max_length=20)
    order_id = models.CharField(max_length=20)
    customer = models.CharField(max_length=100)
    address = models.TextField()
    scheduled_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.delivery_id} - {self.customer}"
    
class Payment(models.Model):
    payment_id = models.CharField(max_length=10, unique=True)
    customer_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    method = models.CharField(max_length=50)

    def __str__(self):
        return self.payment_id
    
class Order(models.Model):
    order_id = models.CharField(max_length=10, unique=True)
    customer_id = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=50)
    product_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.customer_id} - {self.product_name} - {self.date}"

class Supply(models.Model):
    supply_id = models.CharField(max_length=20, unique=True)
    supplier = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.supply_id} - {self.product} ({self.quantity}kg)"