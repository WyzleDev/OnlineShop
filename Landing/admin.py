from django.contrib import admin
from Landing import models
from .models import *


# Register your models here.


class userAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'contact_number', 'city']
    search_fields = ['name', 'email']
    search_help_text = "Поиск по имени или Email"

    class Meta:
        model = User


admin.site.register(User, userAdmin)
