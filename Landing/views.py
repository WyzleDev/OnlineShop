from django.shortcuts import render
from .forms import RegisterUser
from Productz.models import ProductImage
from sitebanners.models import Banner

def home_page(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    banners = Banner.objects.filter(is_active=True)
    return render(request, "index/home.html", locals())
