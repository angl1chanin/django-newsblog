# Generated by Django 4.1.4 on 2022-12-24 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, default="avatars/default.svg", upload_to="avatars/"
            ),
        ),
    ]
