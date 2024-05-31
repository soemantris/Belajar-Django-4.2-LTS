from django.db import models
from django.utils.text import slugify

# Create your models here.


class Tujuan(models.Model):
    nm_penumpang = models.CharField(max_length=50, blank=True)
    nm_pengemudi = models.CharField(max_length=50)
    tujuan = models.TextField()
    profile = models.ImageField(
        blank=True,
        default='profil.png',
        upload_to='profiles/',
    )
    slug = models.SlugField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nm_penumpang)
        super(Tujuan, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.id, self.nm_penumpang)
