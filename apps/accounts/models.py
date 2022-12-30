from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", default='avatars/default.svg', blank=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        kwargs = {
            'username': self.username,
        }
        return reverse_lazy('news:profile-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email.split("@")[0]
        super(User, self).save()
