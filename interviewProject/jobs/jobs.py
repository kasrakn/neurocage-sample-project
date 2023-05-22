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
            SensorData.objects.create(
                cage=cage,
                health_status=health_status,
            )
        elif response.status_code == 503:
            health_status = None
            SensorData.objects.create(
                cage=cage,
                health_status=health_status,
            )
        else:
            pass

        try:
            print(f"-- {cage.id} | status = {health_status}")
        except:
            print(f"calling api for cage {cage.id} failed")
