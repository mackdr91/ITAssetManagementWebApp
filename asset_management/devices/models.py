from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        unique_together = (('name', 'address'),)  # Enforcing combination of name and address to be unique
    

    def __str__(self):
        return self.name
"""
def get_default_location():
    default_location, _ = Location.objects.get_or_create(name="Default", defaults={'address': 'Default Address'})
    return default_location.id
    """

class Device(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    purchase_date = models.DateField(null=True, blank=True)
    warranty_expiry_date = models.DateField()
    serial_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='devices') #default=get_default_location

    def __str__(self):
        return self.name
    


