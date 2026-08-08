from django.db import models


class Appliance(models.Model):
    name = models.CharField(max_length=100)
    power_watts = models.FloatField()
    hours_per_day = models.FloatField()
    days_per_month = models.IntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def daily_consumption(self):
        return (self.power_watts * self.hours_per_day) / 1000

    def monthly_consumption(self):
        return self.daily_consumption() * self.days_per_month

    def __str__(self):
        return self.name