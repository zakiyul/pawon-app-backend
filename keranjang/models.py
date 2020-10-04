from django.db import models
from makanan.models import Makanan


class Keranjang(models.Model):
    jumlah_pesanana = models.FloatField()
    keterangan = models.CharField(max_length=500)
    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
