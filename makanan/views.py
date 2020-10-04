from django.shortcuts import render
from rest_framework import viewsets
from .models import Makanan
from .serializers import MakananSerializer


class MakananView(viewsets.ModelViewSet):
    queryset = Makanan.objects.all()
    serializer_class = MakananSerializer
