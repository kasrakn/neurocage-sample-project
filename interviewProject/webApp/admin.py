from django.contrib import admin
from webApp.models import Cage, SensorData
# Register your models here.

class CageAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'latest_health_status')

class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'cage', 'health_status', 'is_successful')
    exclude = ('is_successful',)

admin.site.register(Cage, CageAdmin)
admin.site.register(SensorData, SensorDataAdmin)