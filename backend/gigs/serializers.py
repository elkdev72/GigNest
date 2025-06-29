from rest_framework import serializers

from .models import Gig

class GigSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Gig
        fields = '__all__'
        read_only_fields = ['id', 'owner', 'created_at']
