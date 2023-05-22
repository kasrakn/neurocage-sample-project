from celery import shared_task, Celery
from celery.schedules import crontab, timedelta
from celery.utils.log import get_task_logger
from webApp.models import Cage, SensorData
import os
import requests




@shared_task
def call_api_for_cage():
    for cage in Cage.objects.all():
        response = requests.get(
            url='http://{}:5000/data/{}'.format(os.getenv('SENSOR_HOST'), cage.id)
        )

        if response.status_code == 200:
            sensor_data = response.json()
            SensorData.objects.create(
                cage=cage,
                health_status=sensor_data['status']
            )
        elif response.status_code == 503:
            SensorData.objects.create(
                cage=cage,
                health_status=None
            )
        else:
            pass


# app.conf.beat_schedule = {
#     'call-api-every-minute': {
#         'task': 'webApp.tasks.call_api_for_cage',
#         # 'schedule': crontab(minute='*/1')
#         'schedule': 10
#     },
# }