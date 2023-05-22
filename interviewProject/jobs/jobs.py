from webApp.models import Cage, SensorData
import requests

def get_sensor_data():
    cages = Cage.objects.all()

    url = "http://localhost:5000/data/"

    for cage in cages:
        req_url = url + str(cage.id)
        response = requests.get(req_url)
        
        if response.status_code == 200:
            health_status = response.json()['status']
        else:
            health_status = None
        SensorData.objects.create(
            cage=cage,
            health_status=health_status,
        )

        print(f"-- {cage.id} | status = {health_status}")
