from django.db import models

# Create your models here.


class Makanan(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.FloatField()
    rating = models.FloatField()
    gambar = models.ImageField(upload_to='makanan/')

    def __str__(self):
        return self.nama
