from django import forms
from .models import Asset,WorkOrder,Technician, SparePart

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'description']  



class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['title', 'description', 'asset', 'technician']  



class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = ['name', 'skills']  




class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = ['name', 'description', 'quantity', 'unit_price']  


