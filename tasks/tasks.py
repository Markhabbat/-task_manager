from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_mail_task(email, task_id):
    send_mail(
        "You have new task",
        f"Task id - {task_id}",
        settings.DEFAULT_FROM_EMAIL,
        [email, ],
        fail_silently=False
    )
