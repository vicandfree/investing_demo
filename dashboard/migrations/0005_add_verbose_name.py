# Generated by Django 4.1.7 on 2023-03-19 02:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0004_add_last_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="share",
            name="name",
            field=models.CharField(
                max_length=255, verbose_name="Наименование компании"
            ),
        ),
    ]
