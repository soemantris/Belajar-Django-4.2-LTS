
from django.contrib import admin
from django.urls import path

from . views import *

urlpatterns = [
    path('change_password/', change_password, name='change_password'),
    path('ubah_password/', ubah_password, name='ubah_password'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]
