from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Location(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label
    
    class Meta:
        ordering = ['label']

class Vehicle(models.Model):
    class VehicleType(models.TextChoices):
        ELECTRIQUE = 'ELECTRIQUE'
        ESSENCE = 'ESSENCE'
        DIESEL = 'DIESEL'

    description = models.TextField(default="")
    number = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex=r'^([A-Z]{2}-[0-9]{3}-[A-Z]{2})|([0-9]{1,4}[A-Z]{1,3}[0-9]{2})$',
                message='Invalid format'
            )
        ]
    )
    vehicle_type = models.CharField(
        max_length=15,
        choices=VehicleType.choices,
        default=VehicleType.ESSENCE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.number