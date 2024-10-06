from django.db import models
from order.models import Order
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.utils import timezone
# Create your models here.

class OrderNotification(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orders')
    notified = models.BooleanField(default=False, verbose_name='notification of order')
    
    def __str__(self):
        return f"Order is {self.order.job_title} by student {self.order.student_name}"
    
    
