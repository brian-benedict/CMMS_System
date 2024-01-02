from django.db import models
from authentication.models import CustomUser


class Asset(models.Model):
    asset_name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    purchase_date = models.DateField()
    maintenance_interval = models.IntegerField()  # Interval in days
    def __str__(self):
        return self.asset_name
    

class MaintenanceTask(models.Model):
    task_name = models.CharField(max_length=255)
    task_description = models.TextField(null=True)
    priority = models.CharField(max_length=50, null=True)
    estimated_duration = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    category = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.task_name



class Technician(models.Model):
    technician_name = models.CharField(max_length=255)
    technician_contact_info = models.TextField()
    def __str__(self):
        return self.technician_name
    

# class SparePart(models.Model):
#     part_name = models.CharField(max_length=255)
#     part_description = models.TextField()
#     quantity_on_hand = models.PositiveIntegerField()
#     reorder_point = models.PositiveIntegerField()
#     vendor = models.CharField(max_length=255)
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    



class MaintenanceHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    work_order = models.ForeignKey('workorder.WorkOrder', on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    notes = models.TextField()


class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

