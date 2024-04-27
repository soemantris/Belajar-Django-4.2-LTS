from django.db import models

# built-in validators
from django.core import validators


# Create your models here.
# import validasi
from .validation import validate_penulis, validate_tag


class Artikel(models.Model):
    judul = models.CharField(
        max_length=100,
        validators=[validators.MaxLengthValidator(7)]
    )
    isi = models.TextField()
    DFT_KATEGORI = (
        ('berita', 'Berita'),
        ('blog', 'Blog'),
        ('jurnal', 'Jurnal'),
    )
    kategori = models.CharField(
        max_length=20,
        choices=DFT_KATEGORI,
        default='blog',
    )
    penulis = models.CharField(
        max_length=25,
        validators=[validate_penulis],
    )
    tag = models.CharField(max_length=25, validators=[validate_tag],)
    penerbit = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.id, self.judul)
