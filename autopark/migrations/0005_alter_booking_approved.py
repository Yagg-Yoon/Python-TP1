# Generated by Django 4.2.1 on 2023-06-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autopark", "0004_booking"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking", name="approved", field=models.BooleanField(null=True),
        ),
    ]
