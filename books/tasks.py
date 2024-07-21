from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings

@shared_task
def send_liked_books_email():
    users = User.objects.all()
    for user in users:
        liked_books = user.liked_books.all()
        if liked_books:
            subject = 'Your Liked Books'
            message = render_to_string('books/email_liked_books.html', {'user': user, 'liked_books': liked_books})
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

# Add this to __init__.py
from __future__ import absolute_import, unicode_literals
from celery import app as celery_app

__all__ = ('celery_app',)
