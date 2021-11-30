from rest_framework import serializers
from .models import Moisture


class MoistureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moisture
        fields = ('id', 'plant_id', 'level', 'created', 'plant_type')
