from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Кастомная модель пользователя"""
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")

    def __str__(self):
        return self.username
