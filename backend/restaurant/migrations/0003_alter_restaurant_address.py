# Generated by Django 4.2.7 on 2024-02-19 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_restaurant_address_restaurant_closing_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="address",
            field=models.CharField(
                help_text="Restaurant Address", max_length=100, verbose_name="Address"
            ),
        ),
    ]