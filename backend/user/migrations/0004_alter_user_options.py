# Generated by Django 4.2.7 on 2024-02-08 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('test_user', 'Just for test')]},
        ),
    ]
