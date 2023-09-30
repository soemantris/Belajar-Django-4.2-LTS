from django.urls import path

from . import views

app_name="kontak"
urlpatterns = [
    path('', views.index),
]
