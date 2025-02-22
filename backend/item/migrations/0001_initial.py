# Generated by Django 4.2.7 on 2025-02-22 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0001_initial"),
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Unit",
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
                ("name", models.CharField(max_length=20, unique=True)),
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
        migrations.CreateModel(
            name="ItemType",
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
                ("name", models.CharField(max_length=20, unique=True)),
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
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=20)),
                (
                    "item_state",
                    models.CharField(
                        choices=[
                            ("hot", "hot"),
                            ("cold", "cold"),
                            ("normal", "normal"),
                            ("frozen", "frozen"),
                            ("liquid", "liquid"),
                        ],
                        default="normal",
                        help_text="Select a Item State",
                        verbose_name="Item State",
                    ),
                ),
                (
                    "item_flavor",
                    models.CharField(
                        choices=[
                            ("sweet", "sweet"),
                            ("spicy", "spicy"),
                            ("salty", "salty"),
                            ("sour", "sour"),
                            ("bitter", "bitter"),
                            ("savory", "savory"),
                            ("groove", "groove"),
                            ("none", "none"),
                        ],
                        default="none",
                        help_text="Select a Item Flavor",
                        verbose_name="Item Flavor",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Set a Item Price",
                        max_digits=15,
                        verbose_name="Price of Item",
                    ),
                ),
                (
                    "max_order_qty",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Set a Max order Qty",
                        max_digits=5,
                        verbose_name="Max Order Qty",
                    ),
                ),
                (
                    "min_order_qty",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Set a Min order Qty",
                        max_digits=5,
                        verbose_name="Min Order Qty",
                    ),
                ),
                (
                    "discount_rate",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Set a discount rate",
                        max_digits=5,
                        verbose_name="Discount Rate",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "active"),
                            ("inactive", "inactive"),
                            ("obsolete", "obsolete"),
                            ("waiting", "waiting"),
                            ("deleted", "deleted"),
                        ],
                        default="active",
                        help_text="Select a Item Status",
                        verbose_name="Item Status",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        default=1,
                        help_text="Select a Category",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="category_items",
                        to="category.category",
                        verbose_name="Category",
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
                    "item_type",
                    models.ForeignKey(
                        help_text="Select a Item Type",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="item_type_items",
                        to="item.itemtype",
                        verbose_name="Item Type",
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        help_text="Select a Store",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="store_items",
                        to="store.store",
                        verbose_name="Store",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        help_text="Select a Unit",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="item.unit",
                        verbose_name="Unit",
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
