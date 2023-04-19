<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.db import models
from .choices import Role


class Seller(models.Model):
    seller = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        related_name='seller',
        limit_choices_to={'user_type': Role.SELLER}
    )

    shop = models.ForeignKey(to='shop.Shop', on_delete=models.DO_NOTHING, related_name='seller_shops')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
=======
from django.db import models

# Create your models here.
>>>>>>> f75d9273045ce67d07b6d7eb5b12529bfc1782ac
