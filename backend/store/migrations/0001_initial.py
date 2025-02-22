# Generated by Django 4.2.7 on 2025-02-22 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Store",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique ID",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        help_text="Unique Code", max_length=120, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the Store",
                        max_length=15,
                        verbose_name="Store",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        help_text="Store Address",
                        max_length=100,
                        verbose_name="Address",
                    ),
                ),
                (
                    "picture",
                    models.URLField(
                        blank=True,
                        default=None,
                        help_text="URL of profile picture",
                        null=True,
                        verbose_name="Profile picture URL",
                    ),
                ),
                (
                    "opening_time",
                    models.TimeField(
                        help_text="Opening time", verbose_name="Opening time"
                    ),
                ),
                (
                    "closing_time",
                    models.TimeField(
                        help_text="Closing time", verbose_name="Closing time"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "active"),
                            ("inactive", "inactive"),
                            ("not-verified", "not-verified"),
                            ("verified", "verified"),
                        ],
                        default="not-verified",
                        help_text="Store status",
                        verbose_name="status",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
