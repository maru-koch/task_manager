import os
import json
from celery import shared_task
from datetime import datetime

@shared_task
def send_notification(task_title:str, user_first_name:str):
    """ Asynchronously send notification. """
    print(f"Task - '{task_title}' completed by {user_first_name} - {datetime.now()}")