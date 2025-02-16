# Generated by Django 4.2.7 on 2024-08-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_car_body_type_car_color_car_drive_unit_car_fuel_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="color",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="car",
            name="model",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="volume",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=4, null=True
            ),
        ),
    ]
