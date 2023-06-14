import django_filters
from autopark.models import Vehicle

class VehicleFilter(django_filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = {
            'number': ['exact', 'contains', 'startswith'],
            'vehicle_type': ['exact'],
            'created_at': ['date', 'year', 'month', 'day', 'gt', 'lt'],
        }
