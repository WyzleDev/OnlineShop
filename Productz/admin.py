from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


class ProductAdminInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    title = _("Product")
    list_display = ["id", "name", "product_price"]
    inlines = [ProductAdminInline]
    search_fields = ["name"]
    search_help_text = "Поиск товаров по имени"
    list_filter = ['product_price']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)
