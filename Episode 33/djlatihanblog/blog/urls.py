from django.urls import path

from .import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<slug:slugInput>/', views.detail_artikel, name='detail_artikel'),
    path('kategori/<slug:kategoriInput>/',
         views.kategori_artikel, name='kategori_artikel')
]
