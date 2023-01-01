from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy

from accounts.models import User
from news.utils import slugify_title, slugify_str, rename_photo_to_slug


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(max_length=150, unique=True, db_index=True, blank=True, null=True, verbose_name="Slug")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", null=True)
    content = models.TextField(blank=True, verbose_name="Статья")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, verbose_name="Категория")
    tags = models.ManyToManyField("Tag", blank=True)
    upvotes = models.PositiveIntegerField(default=0, editable=False, verbose_name="Лайки")
    downvotes = models.PositiveIntegerField(default=0, editable=False, verbose_name="Дизлайки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        context = {
            "category": self.category.slug,
            "article_title": self.slug
        }

        return reverse_lazy("news:article-detail", kwargs=context)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_title(self.title)
        super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(max_length=150, unique=True, verbose_name="Slug")
    photo = models.ImageField(upload_to="categories/")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        context = {
            "category": self.slug,
        }

        return reverse_lazy("news:category", kwargs=context)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_str(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    slug = models.SlugField(max_length=30, unique=True, null=True, verbose_name="Slug")

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:tags-list')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_str(self.title)
        super().save(*args, **kwargs)
