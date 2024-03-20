# Generated by Django 4.2.7 on 2024-02-17 17:05

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="address",
            field=models.CharField(
                default="", help_text="Address", max_length=100, verbose_name="Address"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="restaurant",
            name="closing_time",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="Closing time",
                verbose_name="Closing time",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="restaurant",
            name="code",
            field=models.CharField(
                default="", help_text="Code for %(class)", max_length=120
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="restaurant",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="restaurant",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="name",
            field=models.CharField(
                default="",
                help_text="Name of the Restaurant",
                max_length=15,
                verbose_name="Restaurant",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="restaurant",
            name="opening_time",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="Opening time",
                verbose_name="Opening time",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="restaurant",
            name="picture",
            field=models.URLField(
                blank=True,
                default=None,
                help_text="URL of profile picture",
                null=True,
                verbose_name="Profile picture URL",
            ),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="status",
            field=models.CharField(
                choices=[
                    ("active", "active"),
                    ("inactive", "inactive"),
                    ("not-verified", "not-verified"),
                    ("verified", "verified"),
                ],
                default="not-verified",
                help_text="Restaurant status",
                verbose_name="status",
            ),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                help_text="Unique ID",
                unique=True,
                verbose_name="UUID",
            ),
        ),
    ]
