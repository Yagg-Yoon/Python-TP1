# Generated by Django 4.2.1 on 2023-05-31 13:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("autopark", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=255)),
            ],
            options={"ordering": ["label"],},
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        max_length=9,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Invalid format",
                                regex="^([A-Z]{2}-[0-9]{3}-[A-Z]{2})|([0-9]{1,4}[A-Z]{1,3}[0-9]{2})$",
                            )
                        ],
                    ),
                ),
                (
                    "vehicle_type",
                    models.CharField(
                        choices=[
                            ("ELECTRIQUE", "Electrique"),
                            ("ESSENCE", "Essence"),
                            ("DIESEL", "Diesel"),
                        ],
                        default="ESSENCE",
                        max_length=15,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="autopark.location",
                    ),
                ),
            ],
        ),
    ]