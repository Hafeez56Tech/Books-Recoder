
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

@shared_task
def send_daily_emails():
    users = User.objects.all()
    for user in users:
        send_email(user)

def send_email(user):
    subject = 'Daily Update'
    message = 'Here is your daily update.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)
