# Generated by Django 4.1.2 on 2022-10-16 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="date_of_birth",
        ),
    ]
