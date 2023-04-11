

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Title')
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    price = models.FloatField(verbose_name='Price')
    description = models.TextField(null=True, verbose_name='Description')
    count = models.IntegerField(default=0, verbose_name='quantity')
    rating = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-rating', '-price')

    def __str__(self):
        return f"{self.name} - {self.category}"

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active,
            'category': self.category.to_json()
        }