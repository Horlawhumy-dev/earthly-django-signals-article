#models.py
from django.db.models.signals import pre_delete, post_delete
from django.contrib.auth.models import User

class Order(models.Model):
    grocery = models.CharField(max_length=250)

@receiver(pre_delete, sender=Order)
def get_order_notification(sender, instance, **kwargs):
    print(f"The {instance.grocery} groceries delete request was received on {datetime.now()}.")

@receiver(post_delete, sender=Order)
def get_order_notification(sender, **kwargs):
    print(f"The grocery was deleted successfully on {datetime.now()}.")
