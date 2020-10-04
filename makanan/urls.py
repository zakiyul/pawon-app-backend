
from django.urls import path, include
from rest_framework import routers
from .views import MakananView

router = routers.DefaultRouter()
router.register('', MakananView)

urlpatterns = [
    path('', include(router.urls))
]
