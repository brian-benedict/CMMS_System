from django import forms
from .models import Asset,WorkOrder,Technician, SparePart

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'description']  # Add more fields as needed



class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['title', 'description', 'asset', 'technician']  # Add more fields as needed



class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = ['name', 'skills']  # Add more fields as needed




class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = ['name', 'description', 'quantity', 'unit_price']  # Add more fields as needed


