from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
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

    last_maintenance_at = models.DateTimeField(null=True, blank=True)
    next_check_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.number
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    booking_from = models.DateTimeField()
    booking_to = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)
    approved = models.BooleanField(null=True)

@receiver(post_save, sender=get_user_model())
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)