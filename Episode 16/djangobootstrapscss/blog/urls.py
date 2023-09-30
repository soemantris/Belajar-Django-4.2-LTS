from django.urls import path

from . import views

app_name="blog"
urlpatterns = [
    path('', views.index),
    path('detail/', views.detail_blog),
]
