from django import forms
from .models import WorkOrder


class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['asset', 'task', 'requester', 'assigned_to', 'scheduled_start_date', 'scheduled_end_date', 'actual_start_date', 'actual_end_date', 'status']
