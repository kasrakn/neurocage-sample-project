from apscheduler.schedulers.background import BackgroundScheduler
from jobs.jobs import get_sensor_data

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_sensor_data, 'interval', seconds=5)
    scheduler.start()