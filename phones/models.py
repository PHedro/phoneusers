from django.db import models


class Phone(models.Model):
    ddd = models.CharField(
        verbose_name='DDD',
        max_length=3,
        null=False,
        blank=False
    )
    number = models.CharField(
        verbose_name='Número',
        max_length=9,
        null=False,
        blank=False
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
