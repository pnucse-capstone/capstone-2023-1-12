# Generated by Django 4.2.1 on 2023-10-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_model", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="full_address",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="road_address",
            field=models.CharField(max_length=100),
        ),
    ]