from django.contrib.auth.models import AbstractUser
from django.db import models


class ConcreteUser(AbstractUser):
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False
    )

    REQUIRED_FIELDS = ['email', 'first_name', 'password']
