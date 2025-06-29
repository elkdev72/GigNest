from django.shortcuts import render

# Create your views here.
# backend/gigs/views.py

from rest_framework import viewsets, permissions
from .models import Gig
from .serializers import GigSerializer

class GigViewSet(viewsets.ModelViewSet):
    queryset = Gig.objects.all().order_by('-created_at')
    serializer_class = GigSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
