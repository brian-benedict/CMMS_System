from django.db import models
from django.conf import settings


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Attending', 'Attending'),
        ('InProgress', 'In Progress'),
        ('Done', 'Done'),
        ('Pending', 'Pending')
    ]
    Name = models.CharField(max_length=100)
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    asset_to_be_serviced = models.ForeignKey('system.Asset', on_delete=models.CASCADE)  # Change to ForeignKey
    service_description = models.TextField()
    engineer_feed = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    user_feed = models.BooleanField(default=False)  # False for NOT, True for DONE

    def __str__(self):
        return f"{self.department} - {self.asset_to_be_serviced}"



# In your models.py

class ServiceRequestSparePart(models.Model):
    service_request = models.ForeignKey('ServiceRequest', on_delete=models.CASCADE)
    spare_part = models.ForeignKey('inventory.SparePart', on_delete=models.CASCADE)
    quantity_demanded = models.PositiveIntegerField()
    quantity_fulfilled = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('service_request', 'spare_part')
