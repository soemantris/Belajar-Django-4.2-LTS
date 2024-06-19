
from django.contrib import admin
from django.urls import path

from . views import *

urlpatterns = [
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]
