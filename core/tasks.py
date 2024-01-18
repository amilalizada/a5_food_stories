from celery import shared_task
import time

@shared_task
def export():
    time.sleep(5)