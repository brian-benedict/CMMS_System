from django.shortcuts import render, redirect, get_object_or_404
from .models import SparePart
from .forms import SparePartForm

def spare_parts_list(request):
    parts = SparePart.objects.all()
    return render(request, 'inventory/spare_parts_list.html', {'parts': parts})

def spare_part_create(request):
    if request.method == 'POST':
        form = SparePartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spare_parts_list')
    else:
        form = SparePartForm()
    return render(request, 'inventory/spare_part_form.html', {'form': form})

def spare_part_update(request, pk):
    part = get_object_or_404(SparePart, pk=pk)
    if request.method == 'POST':
        form = SparePartForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('spare_parts_list')
    else:
        form = SparePartForm(instance=part)
    return render(request, 'inventory/spare_part_form.html', {'form': form})

def spare_part_delete(request, pk):
    part = get_object_or_404(SparePart, pk=pk)
    if request.method == 'POST':
        part.delete()
        return redirect('spare_parts_list')
    return render(request, 'inventory/spare_part_confirm_delete.html', {'part': part})
