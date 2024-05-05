from django.urls import path

from . import views

app_name = 'pulangpergi'
urlpatterns = [
    path('delete/<slug:nm_slug>/', views.delete, name='delete'),
    path('create/', views.add_tujuan, name='create'),
    path('', views.index, name='index'),
]
