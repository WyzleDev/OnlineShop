from django.contrib import admin
from .models import *


class BannerAdmin(admin.ModelAdmin):
    list_display = ['banner_name', 'placed_on', 'is_active']

    class Meta:
        model = Banner


admin.site.register(Banner, BannerAdmin)
