from django.shortcuts import render
from rest_framework import viewsets
from .serializers import KeranjangSerializer
from .models import Keranjang


class KeranjangView(viewsets.ModelViewSet):
    queryset = Keranjang.objects.all()
    serializer_class = KeranjangSerializer
