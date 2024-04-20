from django.db import models

# Create your models here.


class Artikel(models.Model):
    judul = models.CharField(max_length=100)
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
    penulis = models.CharField(max_length=25)
    tag = models.CharField(max_length=25)
    penerbit = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.id, self.judul)
