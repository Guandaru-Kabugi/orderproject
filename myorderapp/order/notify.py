from order.models import Order
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.utils import timezone
from notification.models import OrderNotification
def send_notification_for_jobs_due_that_day(sender,created,instance,**kwargs):
    #we want an order that has been created
    if created==False:
        if instance.due_date == timezone.now().date():
            notification = OrderNotification.objects.create(order=instance, notified=False)
            send_mail(
                subject=f'Notification that {notification.order.job_title} is due todau',
                            message='Hello! you have an order due today.', 
                            from_email='guandarualex3@gmail.com',  
                            recipient_list=['kabugi96@gmail.com'], 
                            fail_silently=False,
            )
            notification.notified = True
            notification.save()
            
post_save.connect(receiver=send_notification_for_jobs_due_that_day,sender=Order)