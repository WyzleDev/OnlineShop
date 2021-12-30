from django.urls import include, path

from Landing import views

urlpatterns = [
    path('', views.index, name='Landing page')
]