from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('artikel/', views.daftar_artikel, name='daftar'),
    path('detail/<slug:input>/', views.detail_artikel, name='detail'),
    path('spesial/<int:inputInt>/', views.spesial_artikel, name='spesial'),
]
