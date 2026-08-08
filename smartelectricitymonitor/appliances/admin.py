from django.contrib import admin
from .models import Appliance


@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'power_watts',
        'hours_per_day',
        'days_per_month',
        'daily_usage',
        'monthly_usage',
        'created_at',
    )

    @admin.display(description='Daily Usage (kWh)')
    def daily_usage(self, obj):
        return round(obj.daily_consumption(), 2)

    @admin.display(description='Monthly Usage (kWh)')
    def monthly_usage(self, obj):
        return round(obj.monthly_consumption(), 2)