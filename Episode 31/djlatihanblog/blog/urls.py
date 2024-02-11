from django.urls import path

from .import views

app_name = 'blog'
urlpatterns = [
    path('', views.index),
    path('detail/<slug:slugInput>/', views.detail_artikel),
    path('kategori/<slug:kategoriInput>/', views.kategori_artikel)
]
