from django.core.signals import pre_init
from datetime import datetime

@receiver(pre_init, sender=User)
def callback(sender, **kwargs):
    print(f"User model __init()__  method is called initially at {datetime.now()}")
