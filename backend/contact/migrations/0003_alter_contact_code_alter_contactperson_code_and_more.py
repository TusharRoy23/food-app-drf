# Generated by Django 4.2.7 on 2024-02-19 03:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0002_contactperson_address_alter_contactperson_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="code",
            field=models.CharField(help_text="Unique Code", max_length=120),
        ),
        migrations.AlterField(
            model_name="contactperson",
            name="code",
            field=models.CharField(help_text="Unique Code", max_length=120),
        ),
        migrations.AlterField(
            model_name="contactperson",
            name="contact",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="contact_person_contact",
                to="contact.contact",
                verbose_name="Contact Person",
            ),
        ),
    ]
