# Generated by Django 4.1.7 on 2023-03-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0001_add_share"),
    ]

    operations = [
        migrations.AlterField(
            model_name="share",
            name="figi",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="share",
            name="ticker",
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
