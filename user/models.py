from django.contrib.auth.models import AbstractUser
from django.db import models


class ConcreteUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
        error_messages={
            'unique': "Usuário com esse email já existe.",
        },
    )

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

    token = models.CharField(
        max_length=36,
        null=True,
        blank=True,
        default='',
        unique=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'password']

    @property
    def name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name if self.first_name else '',
            last_name=self.last_name if self.last_name else ''
        ).strip()
