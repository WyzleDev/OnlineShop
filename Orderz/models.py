from django.db import models
from Productz.models import Product


class Status(models.Model):
    status_name = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Статус: %s" % self.status_name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы заказа"


class Order(models.Model):
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_comment = models.TextField(max_length=256, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Заказ №%s %s" % (self.id, self.status.status_name)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, models.CASCADE, blank=True, null=True, default=None)
    number_of_products = models.IntegerField(default=1)
    price_per_product = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
