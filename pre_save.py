from django.db.models.signals import pre_save

class Profile(models.Model):
    to_receive_new_user = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @receiver(pre_save, sender=User)
    def update_profile(sender, instance, **kwargs):
    	instance.to_receive_new_user = True
    	instance.save()
    	return instance
