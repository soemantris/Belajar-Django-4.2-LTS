from django.db import models
from django.utils.text import slugify

# Create your models here.


class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    isi = models.TextField()
    kategori = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, editable=False)
    pubdate = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul)
        return super(Artikel, self).save(*args, **kwargs)

    def __str__(self):
        return self.judul
