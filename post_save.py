from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    is_new_user_created = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=User)
def update_profile(sender, created, instance, **kwargs):
    if created:
        instance.is_new_user_created = True
        instance.save()
    return instance
