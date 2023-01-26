from django.core.signals import request_finished

def get_notified(sender, **kwargs):
    """ Printing a notification string. """
    print("HTTP request finished")
    

request_finished.connect(get_notified)