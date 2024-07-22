
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from .models import Book
from django.template.loader import render_to_string
@shared_task
def send_daily_emails():
    users = User.objects.all()
    for user in users:
        send_email(user)

def send_email(user):
    books =Book.objects.filter(author=user)
    subject = 'Daily Update'
    message = render_to_string('Here is your daily update.', {'books':books})
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)
