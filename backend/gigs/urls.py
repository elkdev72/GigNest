# backend/gigs/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GigViewSet

router = DefaultRouter()
router.register(r'gigs', GigViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
