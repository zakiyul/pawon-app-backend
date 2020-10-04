from rest_framework import serializers
from .models import Makanan


class MakananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Makanan
        fields = ('id', 'nama', 'harga', 'rating', 'gambar')
