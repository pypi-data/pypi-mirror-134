from rest_framework import serializers
from .models import AuxSilo

class AuxSiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxSilo
        fields = ['id', 'name', 'data', 'link', 'time']
