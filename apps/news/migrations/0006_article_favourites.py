# Generated by Django 4.1.4 on 2023-01-05 14:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("news", "0005_alter_article_content_alter_article_photo_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="favourites",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                related_name="favourite",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
