from django.db import models

class WheatherReport(models.Model):
    countfield = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    tz_id = models.CharField(max_length=50)
    localtime = models.DateTimeField()
    lat = models.DecimalField(max_digits=5,decimal_places=2)
    lon = models.DecimalField(max_digits=5,decimal_places=2)
    last_updated = models.DateTimeField()
    temp_c = models.DecimalField(max_digits=5,decimal_places=2)
    humidity = models.DecimalField(max_digits=5,decimal_places=2)
    feelslike_c = models.DecimalField(max_digits=5,decimal_places=2)
    wind_dir = models.CharField(max_length=5)

    def __str__(self):
        return self.name

#creating a class called WheatherReport using django models (using default database system sqlite3)