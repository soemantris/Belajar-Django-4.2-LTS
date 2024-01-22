from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index),
    path('<slug:kategoriInput>/', views.kategori),
    path('detail/<slug:slugInput>/', views.detail_artikel),
]
