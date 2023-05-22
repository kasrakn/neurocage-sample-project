# interviewProject/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "interviewProject.settings")
app = Celery("interviewProject")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()