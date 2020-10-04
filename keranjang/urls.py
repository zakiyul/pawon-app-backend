from landingPage.urls import urlpatterns
from django.urls import path, include
from rest_framework import routers
from .views import KeranjangView

router = routers.DefaultRouter()
router.register('', KeranjangView)

urlpatterns = [
    path('', include(router.urls))
]
