import time
from celery import shared_task
from food import settings
from django.template.loader import render_to_string
from story.models import Recipe
from core.models import Subscriber
from django.core.mail import EmailMultiAlternatives

@shared_task
def export():
    time.sleep(5)


@shared_task
def send_email():
    subs = list(Subscriber.objects.values_list('email', flat=True))
    recipes = Recipe.objects.all()[:5]
    subject = "New Recipes"
    text_content = "This is an important message."
    for sub in subs:
        message = render_to_string('email-subscribers.html', {
                    "recipes": recipes,
                    "name": sub,
                })
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [sub])
        msg.attach_alternative(message, "text/html")
        msg.send()
    