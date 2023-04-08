from django.contrib import admin

from cars.models import Car

# admin.site.register(Car)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['license_plate','brand','model']
    list_filter = ['license_plate','brand','model', 'color', 'year', 'redder_location', 'engine_volume']
