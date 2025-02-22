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
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ContactGroup",
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
                        blank=True,
                        help_text="Contact Group Name",
                        max_length=25,
                        verbose_name="Name",
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
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContactGroup",
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
                    "contact_group",
                    models.ForeignKey(
                        help_text="Contact Group",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_groups",
                        related_query_name="contact_group",
                        to="contact.contactgroup",
                        verbose_name="Contact Group",
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
                    "django_group",
                    models.ForeignKey(
                        help_text="Django Group",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="django_groups",
                        related_query_name="django_group",
                        to="auth.group",
                        verbose_name="Django Group",
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
            name="ContactPerson",
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
                    "address",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=120,
                        null=True,
                        verbose_name="Contact Person address",
                    ),
                ),
                ("is_store_owner", models.BooleanField(default=False)),
                ("is_store_user", models.BooleanField(default=False)),
                (
                    "contact",
                    models.ForeignKey(
                        help_text="Contact for person",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contact_person_contact",
                        to="contact.contact",
                        verbose_name="Contact",
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
                (
                    "user",
                    models.OneToOneField(
                        help_text="Contact person user",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="contact_person_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="contactgroup",
            name="django_groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="Contact Group",
                related_name="contact_groups",
                through="contact.DjangoContactGroup",
                to="auth.group",
                verbose_name="Contact Group",
            ),
        ),
        migrations.AddField(
            model_name="contactgroup",
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
            model_name="contact",
            name="contact_group",
            field=models.ForeignKey(
                blank=True,
                help_text="Contact Group",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="contacts",
                to="contact.contactgroup",
            ),
        ),
        migrations.AddField(
            model_name="contact",
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
            model_name="contact",
            name="store",
            field=models.ForeignKey(
                blank=True,
                help_text="For store user",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="contact_store",
                to="store.store",
                verbose_name="Store",
            ),
        ),
        migrations.AddField(
            model_name="contact",
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
    ]
