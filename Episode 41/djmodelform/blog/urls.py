from django.urls import path

from .views import index, create_artikel

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create_artikel, name='create'),
]
