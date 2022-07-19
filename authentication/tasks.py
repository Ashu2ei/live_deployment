from celery import task
from django.core.mail import send_mail

@task(name="send_request_access_mail")
def send_request_access_mail(subject, message, sender, receivers):
    send_mail(subject, message, sender, receivers)