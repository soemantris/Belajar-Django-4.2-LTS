
from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^(?P<tahun>[0-9]{4})/$', views.thn_arsip),
    path('<int:input>/', views.arsip),
    path('<int:tgl>/<int:bln>/<int:thn>/', views.tgl_arsip),
    path('<slug:kategori>/', views.detail_arsip),
    path('admin/', admin.site.urls),
]
