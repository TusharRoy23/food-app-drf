# Generated by Django 4.2.7 on 2024-02-19 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0007_alter_user_email_alter_user_is_active"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_restaurant_owner",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_restaurant_user",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_visitor",
        ),
    ]
