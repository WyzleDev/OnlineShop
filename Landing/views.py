import time
import datetime

from django.shortcuts import render
from .forms import RegisterUser


def index(request):
    name = 'Cod'
    today_is = datetime.datetime.now()
    form = RegisterUser(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form)
        data = form.cleaned_data
        print(data['name'])
        new_form = form.save()
    return render(request, 'index/index.html', locals())
