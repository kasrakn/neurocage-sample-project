from django.db import models
from timescale.db.models.fields import TimescaleDateTimeField
from timescale.db.models.models import TimescaleModel
from timescale.db.models.managers import TimescaleManager
# Create your models here.

class Cage(models.Model):
    label = models.CharField(max_length=255)

    @property
    def latest_health_status(self):
        row = SensorData.objects.filter(cage=self, is_successful=True).last()  
        return row.health_status if row != None else None
    
    def __str__(self) -> str:
        return self.label


class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    cage = models.ForeignKey(Cage, on_delete=models.CASCADE, related_name='sensor_data_rows')
    health_status = models.IntegerField(null=True, blank=True)
    is_successful = models.BooleanField(null=False)

    def save(self, *args, **kwargs):
        self.is_successful = self.health_status in [1, 2, 3]
        super(SensorData, self).save(*args, **kwargs)

    # time = TimescaleDateTimeField(interval='1 day')
    # objects = models.Manager()
    # timescale = TimescaleManager()