from django.db import models

# Create your models here.


class Kontak(models.Model):
    subjek = models.CharField(max_length=255)
    pesan = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.email
