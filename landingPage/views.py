from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.utils import serializer_helpers
from .serializers import LandingPageSerializer
from .models import LandingPage


class LandingPageView(viewsets.ModelViewSet):
    queryset = LandingPage.objects.all()
    serializer_class = LandingPageSerializer
