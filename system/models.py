from django.db import models
from django.contrib.auth.models import User

class Asset(models.Model):
    asset_name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    purchase_date = models.DateField()
    maintenance_interval = models.IntegerField()  # Interval in days
    # Add other asset-related fields

class MaintenanceTask(models.Model):
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    frequency = models.IntegerField()  # Frequency in days
    # Add other task-related fields

class Technician(models.Model):
    technician_name = models.CharField(max_length=255)
    technician_contact_info = models.TextField()
    # Add other technician-related fields

class SparePart(models.Model):
    part_name = models.CharField(max_length=255)
    part_description = models.TextField()
    quantity_on_hand = models.PositiveIntegerField()
    reorder_point = models.PositiveIntegerField()
    vendor = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other spare part-related fields

class WorkOrder(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    task = models.ForeignKey(MaintenanceTask, on_delete=models.CASCADE)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Technician, on_delete=models.CASCADE)
    scheduled_start_date = models.DateTimeField()
    scheduled_end_date = models.DateTimeField()
    actual_start_date = models.DateTimeField(null=True, blank=True)
    actual_end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50)
    # Add other work order-related fields

class MaintenanceHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    notes = models.TextField()
    # Add other maintenance history-related fields

class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Add fields for report criteria, results, or any other relevant data

# Define other models as needed for your CMMS
