from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First name')
    last_name = models.CharField(max_length=100, verbose_name='Last name')
    phone_number = models.CharField(max_length=50, verbose_name='Phone number')
    email = models.EmailField(max_length=255, verbose_name='Email')
    address = models.CharField(max_length=255, verbose_name='Address')
    city = models.CharField(max_length=150, verbose_name='City')
    delivery_time = models.DateTimeField(verbose_name='Delivery time')
    paid = models.BooleanField(default=False, verbose_name='Paid for order')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', '-updated_at',)

    def __str__(self):
        return f'{self.pk}. {self.address} - {self.phone_number}'

    def get_total_price(self):
        return sum(item.get_price() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id} ({self.product}) --> {self.order.first_name}'

    def get_price(self):
        return self.quantity * self.product.price
