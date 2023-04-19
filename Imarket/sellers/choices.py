from django.db import models


class Role(models.TextChoices):
    ADMIN = 'Admin'
    SELLER = 'Seller'
    CUSTOMER = 'Customer'
