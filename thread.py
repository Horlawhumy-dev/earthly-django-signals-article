import threading
from smtplib import SMTPException
from auth_system.settings import EMAIL_HOST_USER
from .helper import send_account_otp

class SendForgetPasswordEmail(threading.Thread):
    
    def __init__(self , email , user):
        self.email = email
        self.user = user
        self._otp = 0
        threading.Thread.__init__(self)
    
    def run(self):
        try:
            subject = "@noreply: Your password reset one time password."
            self._otp = send_account_otp(self.email, self.user, subject) #this returns the sent otp
        except SMTPException as e:
            print('There was an error sending an email. '+ e)

    def get_otp(self):
        return self._otp
