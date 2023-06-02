from django import forms
from django.utils import timezone
from autopark.models import Vehicle, Booking

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

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['vehicle', 'booking_from', 'booking_to', 'comments']
        labels = {
            'vehicle': 'Véhicule',
            'booking_from': 'Date et heure de début',
            'booking_to': "Date et heure de fin",
            'comments': 'Commentaires'
        }

    def clean(self):
        cleaned_data = super().clean()
        vehicle = cleaned_data.get('vehicle')
        booking_from = cleaned_data.get('booking_from')
        booking_to = cleaned_data.get('booking_to')

        if booking_from and booking_to and booking_from >= booking_to:
            self.add_error('booking_from', 'La date et l\'heure de début doivent être antérieures à la date et l\'heure de fin.')

        current_datetime = timezone.now()
        if booking_from and booking_from <= current_datetime:
            self.add_error('booking_from', 'La réservation doit être faite pour une date et heure futures.')

        if vehicle and booking_from and booking_to:
            conflicting_bookings = Booking.objects.filter(vehicle=vehicle).exclude(pk=self.instance.pk).filter(
                booking_from__lt=booking_to, booking_to__gt=booking_from
            )
            if conflicting_bookings.exists():
                self.add_error('booking_from', 'Ce véhicule est déjà réservé sur ce créneau.')

        return cleaned_data
