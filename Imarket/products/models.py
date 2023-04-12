from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True, verbose_name='Image')
    price = models.FloatField(verbose_name='Price')
    description = models.TextField(null=True, verbose_name='Description')
    count = models.IntegerField(default=0, verbose_name='Quantity')
    rating = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-rating', '-price')

    def __str__(self):
        return f"{self.name} - {self.category}"


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True, verbose_name='Image')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
        ordering = ('-created_at', )

    def __str__(self):
        return f'Image of {self.product.name}'
