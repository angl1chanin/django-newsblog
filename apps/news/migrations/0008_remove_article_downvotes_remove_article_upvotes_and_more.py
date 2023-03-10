# Generated by Django 4.1.4 on 2023-01-09 00:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("news", "0007_remove_article_favourites_article_bookmarks"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="downvotes",
        ),
        migrations.RemoveField(
            model_name="article",
            name="upvotes",
        ),
        migrations.AddField(
            model_name="article",
            name="downvotes",
            field=models.ManyToManyField(
                blank=True,
                related_name="downvotes_article",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Не понравилось",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="upvotes",
            field=models.ManyToManyField(
                blank=True,
                related_name="upvotes_article",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Понравилось",
            ),
        ),
    ]
