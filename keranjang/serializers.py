from rest_framework import serializers
from rest_framework import fields
from .models import Keranjang
from makanan.serializers import MakananSerializer


class KeranjangSerializer(serializers.ModelSerializer):
    # Keranjang.makanan = serializers.RelatedField(many=True, read_only=True)
    makanan = MakananSerializer()

    class Meta:
        model = Keranjang
        fields = ('jumlah_pesanana', 'keterangan', 'makanan')
