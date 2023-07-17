from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class UserRoles(TextChoices):
    MEMBER = "member", "Пользователь"
    ADMIN = "admin", "Админ"
    MODERATOR = "moderator", "Модератор"


class User(AbstractUser):
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    age = models.PositiveIntegerField()
    locations = models.ManyToManyField(Location)

    def save(self, *args, **kwargs):
        self.set_password(raw_password=self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]




