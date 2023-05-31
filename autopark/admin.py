from django.contrib import admin
from .models import Vehicle, Location

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ['label']

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['number', 'vehicle_type', 'location', 'created_at']
    list_filter = ['location']
    search_fields = ['number']

admin.site.register(Location, LocationAdmin)
admin.site.register(Vehicle, VehicleAdmin)