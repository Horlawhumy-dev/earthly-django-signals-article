from django.core.mail import send_mail
from smtplib import SMTPException
from auth_system.settings import EMAIL_HOST_USER

import secrets
        
def send_account_otp(email , user, subject):
    otp = secrets.choice(range(1000, 10000))
    message = f"Hi {user.username},\n\nYour account one-time-password is {otp}.\
        \n This one-time password will expire in the next 10 minutes.\
        \n Kindly supply it to move forward in the pipeline.\n\n\nCheers"
    email_from = EMAIL_HOST_USER
    recipient_list = [email]
    try:
        send_mail(subject, message, email_from, recipient_list)
    except SMTPException as e:
        print('There was an error sending an email. '+ e)
        return
        
    return otp
