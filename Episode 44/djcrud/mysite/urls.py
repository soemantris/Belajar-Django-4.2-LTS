
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('pulangpergi/', include('pulangpergi.urls', namespace='pulangpergi')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
