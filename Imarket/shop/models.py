from django.core.exceptions import ValidationError
from django.db import models


def validate_rating(value):
    if 0 <= value <= 5:
        return value
    else:
        raise ValidationError("This field accepts rating between 0 and 5")


class Shop(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rating = models.FloatField(default=0, verbose_name='Rating', validators=[validate_rating, ])
    address = models.CharField(max_length=255, verbose_name='Shop address', unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
        ordering = ('-rating', 'name')

    def __str__(self):
        return f'{self.pk}, {self.name} ({self.address})'
