from datetime import timezone
from rest_framework import serializers
from .models import Device, Location

class DeviceSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.name', read_only=True)

    class Meta:
        model = Device
        fields = ['id', 'name', 'device_type', 'location', 'location_name']

    def validate_purchase_date(self, value):
        # Example validation: Ensure purchase_date is not in the future
        if value > timezone.now().date():
            raise serializers.ValidationError("Purchase date cannot be in the future.")
        return value

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        
    def validate(self, data):
        # Custom validation logic, if necessary
        return data
