from rest_framework import serializers
from .models import Owner, Service, Car

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    service = ServiceSerializer()
    class Meta:
        model = Car
        fields = '__all__'
