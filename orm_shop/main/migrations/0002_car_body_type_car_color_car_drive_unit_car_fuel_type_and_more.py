# Generated by Django 4.2.7 on 2024-08-22 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="body_type",
            field=models.CharField(
                choices=[
                    ("sedan", "Седан"),
                    ("hatchback", "Хэтчбек"),
                    ("SUV", "Внедорожник"),
                    ("wagon", "Универсал"),
                    ("minivan", "Минивэн"),
                    ("pickup", "Пикап"),
                    ("coupe", "Купе"),
                    ("cabrio", "Кабриолет"),
                ],
                default="sedan",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="color",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name="car",
            name="drive_unit",
            field=models.CharField(
                choices=[("rear", "Задний"), ("front", "Передний"), ("full", "Полный")],
                default="rear",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="fuel_type",
            field=models.CharField(
                choices=[
                    ("gasoline", "Бензин"),
                    ("diesel", "Дизель"),
                    ("hybrid", "Гибрид"),
                    ("electro", "Электро"),
                ],
                default="gasoline",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="gearbox",
            field=models.CharField(
                choices=[
                    ("manual", "Механика"),
                    ("automatic", "Автомат"),
                    ("вариатор", "CVT"),
                    ("robot", "Робот"),
                ],
                default="manual",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="image",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="car",
            name="mileage",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="car",
            name="model",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="car",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="car",
            name="volume",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="car",
            name="year",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="sale",
            name="car",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, to="main.car"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sale",
            name="client",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, to="main.client"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sale",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="car",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
