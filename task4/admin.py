from django.contrib import admin
from task4.models import WheatherReport

class Reports(admin.ModelAdmin):
    list_display = ('countfield', 'name', 'region', 'country', 'tz_id', 'localtime', 'lat', 'last_updated', 'temp_c', 'humidity', 'feelslike_c', 'wind_dir')

admin.site.register(WheatherReport,Reports)

#creating a class to diplay the database named WheatherReport