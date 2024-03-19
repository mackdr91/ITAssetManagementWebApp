from django.urls import path
from .views import DeviceListCreate, LocationListCreate, DevicePartialUpdateView, delete_location

urlpatterns = [
    path('devices/', DeviceListCreate.as_view(), name='device-list-create'),
    path('locations/', LocationListCreate.as_view(), name='location-list-create'),
    path('devices/<int:pk>/', DevicePartialUpdateView.as_view(), name='device-update-delete'),
    path('locations/<int:pk>/', delete_location, name='delete_location'),
    
]
