
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('kontak/', include('kontak.urls', namespace='kontak')),
    path('admin/', admin.site.urls),
]
