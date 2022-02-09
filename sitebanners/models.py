from django.db import models
import random

# Create your models here.

class Banner(models.Model):
    CHOICES = (
        ('Главная страница', 'Главная страница'),
        ('Страница товара', 'Страница товара'),
        ('Другое', 'Другое'),
    )
    id = random.randint(1, 100000)
    banner_name = models.CharField(max_length=64, blank=False, null=False, default=f"{id}", verbose_name='Имя баннера')
    Image = models.ImageField(upload_to='static/static_dev/media/site_banners/', verbose_name="Фото")
    placed_on = models.CharField(max_length=40, choices=CHOICES, default="Главная страница",
                                 verbose_name="На какой странице расположен баннер")
    is_active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.banner_name

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
