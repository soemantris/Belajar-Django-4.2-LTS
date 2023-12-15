from django.contrib import admin

# Register your models here.
from .models import Artikel, Kategori

admin.site.register(Artikel)
admin.site.register(Kategori)
