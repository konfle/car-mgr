from rest_framework import routers
from .viewsets import CarsViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarsViewSet)
