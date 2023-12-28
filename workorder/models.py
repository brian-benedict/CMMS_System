from django.db import models
from authentication.models import CustomUser
from system.models import Asset, MaintenanceTask, Technician

# Create your models here.


class WorkOrder(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    task = models.ForeignKey(MaintenanceTask, on_delete=models.CASCADE)
    requester = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Technician, on_delete=models.CASCADE)
    scheduled_start_date = models.DateTimeField()
    scheduled_end_date = models.DateTimeField()
    actual_start_date = models.DateTimeField(null=True, blank=True)
    actual_end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50)