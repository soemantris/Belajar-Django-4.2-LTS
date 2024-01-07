from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index),
    path('blog/', views.kategori_blog),
    path('berita/', views.berita),
    path('gibah/', views.bukan_gibah),

]
