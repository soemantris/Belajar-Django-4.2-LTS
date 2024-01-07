from django.db import models

# Create your models here.


class Kategori(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} {self.nama}"


class Artikel(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    tanggalPublik = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.judul}"
