from django.db import models

class Station(models.Model):
    """Weather station IMGW."""
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True) #lan
    longitude = models.FloatField(null=True, blank=True) #lot

    def __str__(self):
        return f"{self.name} - {self.code}"


class WeatherMeasurement(models.Model):
    """Weather old and new measurements."""
    station = models.ForeignKey(Station,
                                on_delete=models.CASCADE,
                                related_name='measurements')

    created_at = models.DateTimeField(auto_now_add=True)

    ground_temp = models.FloatField(null=True, blank=True)
    ground_temp_date = models.DateTimeField(null=True, blank=True)

    air_temp = models.FloatField(null=True, blank=True)
    air_temp_date = models.DateTimeField(null=True, blank=True)

    wind_speed = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    rainfall = models.FloatField(null=True, blank=True)

    # Newest measurements will be first
    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['station', 'air_temp_date'],
                name='unique_station_air_temp_date'
            )
        ]

    def __str__(self):
        return f"Measurements for {self.station} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"