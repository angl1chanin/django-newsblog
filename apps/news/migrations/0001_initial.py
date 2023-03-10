# Generated by Django 4.1.4 on 2022-12-24 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=150, verbose_name="Название")),
                (
                    "slug",
                    models.SlugField(max_length=150, unique=True, verbose_name="Slug"),
                ),
                ("photo", models.ImageField(upload_to="categories/")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("title", models.CharField(max_length=30, verbose_name="Название")),
            ],
        ),
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=150, verbose_name="Название")),
                (
                    "slug",
                    models.SlugField(max_length=150, unique=True, verbose_name="Slug"),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="photos/%Y/%m/%d"
                    ),
                ),
                ("content", models.TextField(verbose_name="Статья")),
                (
                    "upvotes",
                    models.PositiveIntegerField(
                        default=0, editable=False, verbose_name="Лайки"
                    ),
                ),
                (
                    "downvotes",
                    models.PositiveIntegerField(
                        default=0, editable=False, verbose_name="Дизлайки"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="news.category",
                        verbose_name="Категория",
                    ),
                ),
                ("tags", models.ManyToManyField(to="news.tag")),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
                "ordering": ["-created_at"],
            },
        ),
    ]
