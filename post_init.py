from django.core.signals import post_init
from datetime import datetime

@receiver(post_init, sender=User)
def callback(sender, instance, **kwargs):
    print(f"User {instance.name} is created at {datetime.now()}")
