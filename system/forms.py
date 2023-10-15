from django import forms
from .models import Asset, WorkOrder, Technician, SparePart, MaintenanceTask

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_name', 'description', 'location', 'purchase_date', 'maintenance_interval']

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['asset', 'task', 'requester', 'assigned_to', 'scheduled_start_date', 'scheduled_end_date', 'actual_start_date', 'actual_end_date', 'status']

class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = ['technician_name', 'technician_contact_info']

class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = ['part_name', 'part_description', 'quantity_on_hand', 'reorder_point', 'vendor', 'unit_price']

class MaintenanceTaskForm(forms.ModelForm):
    class Meta:
        model = MaintenanceTask
        fields = ['task_name', 'task_description', 'priority', 'estimated_duration', 'category']