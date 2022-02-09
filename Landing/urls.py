from django.urls import include, path

from Landing import views

urlpatterns = [
    path('', views.home_page , name='Landing page')
]