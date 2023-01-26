from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def get_notified(sender, **kwargs):
    print("HTTP request finished")