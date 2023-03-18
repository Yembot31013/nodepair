from django.db import models
from meta.models import Overview
from projectApp.models import Project_Overview
from seller.models import Personal_Info
from django.contrib.auth.models import User
import random

# Create your models here.
class Payment(models.Model):
    buyer_address = models.CharField(max_length=50)
    payment_hash = models.CharField(max_length=50)
    smart_contract = models.CharField(max_length=50)
    price = models.IntegerField(blank=True, null=True)
    payed_at = models.DateTimeField(auto_now=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_hash
    

class Meta_Order(models.Model):
    ORDER_STATUS = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Decline', 'Decline'),
        ('Cancelled', 'Cancelled'),
    ]
    order_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    service = models.ForeignKey(Overview, on_delete=models.CASCADE)
    seller = models.ForeignKey(Personal_Info, related_name='seller', on_delete=models.CASCADE, null=True)
    buyer = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='Pending')
    completed = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id
    
    def save(self, *args, **kwargs):
       result = random.choices([1,2,3,4,5,6,7,8,9,0], k=9)
       result = list(map(str, result))
       result = "".join(result)
       result = 'OR' + result
       self.order_id = result

       super(Meta_Order, self).save(*args, **kwargs) # Call the real save() method

# class Project_Order(models.Model):
#     ORDER_STATUS = [
#         ('Completed', 'Completed'),
#         ('Pending', 'Pending'),
#         ('Decline', 'Decline'),
#         ('Cancelled', 'Cancelled'),
#     ]
#     order_id = models.CharField(max_length=50, unique=True)
#     price = models.IntegerField()
#     service = models.ForeignKey(Project_Overview, on_delete=models.CASCADE)
#     seller = models.ForeignKey(Personal_Info, related_name='seller', on_delete=models.CASCADE)
#     buyer = models.ForeignKey(Personal_Info, related_name='client', on_delete=models.CASCADE)
#     country = models.CharField(max_length=100)
#     browser = models.CharField(max_length=100)
#     status = models.CharField(max_length=10, choices=ORDER_STATUS, default='Pending')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.order_id
    
#     def save(self, *args, **kwargs):
#        result = random.choices([1,2,3,4,5,6,7,8,9,0], k=9)
#        result = list(map(str, result))
#        result = "".join(result)
#        result = 'OR' + result
#        self.order_id = result

#        super(Project_Order, self).save(*args, **kwargs) # Call the real save() method
    
