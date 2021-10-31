from django.db.models import fields
from rest_framework import serializers
from .models import Moisture

class MoistureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moisture
        fields = ('id', 'level', 'created')