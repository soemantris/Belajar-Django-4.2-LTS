from django.db import models
from django.utils.text import slugify

# Create your models here.


class Kategori(models.Model):
    nama = models.CharField(max_length=255)
    slug_kat = models.SlugField(editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug_kat = slugify(self.nama)
        return super(Kategori, self).save(*args, **kwargs)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)


class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    isi = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    slug_art = models.SlugField(editable=False, blank=True)
    pubdate = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug_art = slugify(self.judul)
        return super(Artikel, self).save(*args, **kwargs)

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)
