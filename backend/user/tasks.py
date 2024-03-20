from celery import shared_task
from django.core.mail import EmailMessage


@shared_task()
def send_email(to_email, subject, body):
    email = EmailMessage(
        subject=subject,
        body=body,
        to=to_email,
    )

    email.send()
