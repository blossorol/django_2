# Generated by Django 4.2.7 on 2023-11-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("firstapp", "0002_article"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("password", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=20)),
            ],
        ),
    ]
