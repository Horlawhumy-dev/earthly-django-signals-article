from django.db import models
from django.contrib.auth.models import User

class ForgetPassword(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    forget_password_otp = models.CharField(max_length=10 ,null=True, blank=True)
    is_user_password_updated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=ForgetPassword)
def send_email_otp(sender, instance, created, **kwargs):
    try:
        if created:
            """ EXECUTING THREAD TO SEND EMAIL """
            new_thread = SendForgetPasswordEmail(email=instance.email , user=instance.user)
	        new_thread.start()
            new_thread.join() #joining another thread to run one to catch the otp value
            instance.forget_password_otp = new_thread.get_otp()  #setting the user otp
            instance.save()
            return instance
    except SystemError as e:
        print(e)