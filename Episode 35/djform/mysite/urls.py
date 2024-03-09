
from django.contrib import admin
from django.urls import path, include

from . views import index

urlpatterns = [
    path('', index, name='index'),
    path('kontak/', include('kontak.urls', namespace='kontak')),
    path('admin/', admin.site.urls),
]
