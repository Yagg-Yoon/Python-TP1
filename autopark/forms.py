from django import forms
from autopark.models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['description', 'number', 'vehicle_type', 'location']
        exclude = ['created_at']
        labels = {
            'number': 'Plaque d\'immatriculation',
            'vehicle_type': 'Type de véhicule',
            'location': 'Emplacement',
        }
