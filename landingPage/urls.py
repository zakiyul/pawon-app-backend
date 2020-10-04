
from django.urls import path, include
from rest_framework import routers
from .views import LandingPageView

router = routers.DefaultRouter()
router.register('', LandingPageView)

urlpatterns = [
    path('', include(router.urls))
]
