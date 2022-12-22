# Generated by Django 4.1.4 on 2022-12-12 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("playground_app", "0003_alter_playground_created_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("date", models.DateField()),
                ("start_time", models.CharField(max_length=10)),
                ("end_time", models.CharField(max_length=10)),
                ("booking_hours", models.IntegerField(blank=True, null=True)),
                ("total_price_to_be_paid", models.FloatField(blank=True, null=True)),
                (
                    "playground_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="booked_playground",
                        to="playground_app.playground",
                    ),
                ),
                (
                    "reservationist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="booking_user_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]