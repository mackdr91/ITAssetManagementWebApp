from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Device, Location
from .serializers import DeviceSerializer, LocationSerializer
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

# Create your views here.



@api_view(['DELETE'])
def delete_location(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    location.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




class DeviceListCreate(APIView):
    def get(self, request, format=None):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class LocationListCreate(APIView):
    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({'detail': 'A location with this name and address already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=400)



class DevicePartialUpdateView(APIView):
    def patch(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        serializer = DeviceSerializer(device, data=request.data, partial=True) # partial=True for PATCH
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Device ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            device = Device.objects.get(pk=pk)
            device.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Device.DoesNotExist:
            return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Log the exception e if necessary
            return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

