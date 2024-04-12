from django.urls import path

from .views import index, create

app_name = 'kontak'
urlpatterns = [
    path('create/', create, name='create'),
    path('', index, name='index'),
]
