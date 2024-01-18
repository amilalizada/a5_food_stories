import os
from celery import Celery
from food import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food.settings")
app = Celery("celery_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
