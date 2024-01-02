from django.shortcuts import render, redirect, get_object_or_404

# models
from .models import WorkOrder

# forms
from .forms import WorkOrderForm  
from django.contrib.auth.forms import UserCreationForm


# WorkOrder views
def work_order_list(request):
    work_orders = WorkOrder.objects.all()
    return render(request, 'work_order/list.html', {'work_orders': work_orders})


def create_work_order(request):
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_order_list')  # Redirect to work order list view
    else:
        form = WorkOrderForm()
    return render(request, 'work_order/create.html', {'form': form})


def update_work_order(request, work_order_id):
    work_order = get_object_or_404(WorkOrder, id=work_order_id)
    if request.method == 'POST':
        form = WorkOrderForm(request.POST, instance=work_order)
        if form.is_valid():
            form.save()
            return redirect('work_order_list')  # Redirect to work order list view
    else:
        form = WorkOrderForm(instance=work_order)
    return render(request, 'work_order/update.html', {'form': form, 'work_order': work_order})


def delete_work_order(request, work_order_id):
    work_order = get_object_or_404(WorkOrder, id=work_order_id)
    if request.method == 'POST':
        work_order.delete()
        return redirect('work_order_list')  # Redirect to work order list view
