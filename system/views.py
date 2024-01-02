from django.shortcuts import render, redirect, get_object_or_404


# models
from .models import Report
from .models import MaintenanceHistory
from .models import Technician
from .models import Asset
from workorder.models import WorkOrder
from .models import MaintenanceTask

# forms
from .forms import AssetForm  
from .forms import TechnicianForm 
from .forms import MaintenanceTaskForm  
from django.contrib.auth.forms import UserCreationForm


# Dashboard view
def dashboard(request):
    # Fetch relevant data for the dashboard
    total_assets = Asset.objects.count()
    total_maintenance_tasks = MaintenanceTask.objects.count()
    total_work_orders = WorkOrder.objects.count()

    # Pass data to the dashboard template
    context = {
        'total_assets': total_assets,
        'total_maintenance_tasks': total_maintenance_tasks,
        'total_work_orders': total_work_orders,
    }
    
    return render(request, 'dashboard/dashboard.html', context)







# reporting view


def generate_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    # assets = Asset.objects.filter()
    assets = Asset.objects.all()

    context = {
        'report': report,
        'assets': assets,
    }

    return render(request, 'reporting/report.html', context)




# Maintenance history view
def maintenance_history_list(request):
    history_entries = MaintenanceHistory.objects.all()
    return render(request, 'maintenance_history/list.html', {'history_entries': history_entries})





# Maintenance views

def maintenance_task_list(request):
    tasks = MaintenanceTask.objects.all()
    return render(request, 'maintenance_task/list.html', {'tasks': tasks})

def create_maintenance_task(request):
    if request.method == 'POST':
        form = MaintenanceTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_task_list')
    else:
        form = MaintenanceTaskForm()
    return render(request, 'maintenance_task/create.html', {'form': form})

def update_maintenance_task(request, task_id):
    task = get_object_or_404(MaintenanceTask, id=task_id)
    if request.method == 'POST':
        form = MaintenanceTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('maintenance_task_list')
    else:
        form = MaintenanceTaskForm(instance=task)
    return render(request, 'maintenance_task/update.html', {'form': form, 'task': task})

def delete_maintenance_task(request, task_id):
    task = get_object_or_404(MaintenanceTask, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('maintenance_task_list')
    return render(request, 'maintenance_task/delete.html', {'task': task})









# # Spare parts views

# def spare_part_list(request):
#     spare_parts = SparePart.objects.all()
#     return render(request, 'spare_part/list.html', {'spare_parts': spare_parts})

# def create_spare_part(request):
#     if request.method == 'POST':
#         form = SparePartForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('spare_part_list')  # Redirect to spare part list view

#     else:
#         form = SparePartForm()

#     return render(request, 'spare_part/create.html', {'form': form})

# def update_spare_part(request, spare_part_id):
#     spare_part = get_object_or_404(SparePart, id=spare_part_id)

#     if request.method == 'POST':
#         form = SparePartForm(request.POST, instance=spare_part)
#         if form.is_valid():
#             form.save()
#             return redirect('spare_part_list')  # Redirect to spare part list view

#     else:
#         form = SparePartForm(instance=spare_part)

#     return render(request, 'spare_part/update.html', {'form': form, 'spare_part': spare_part})

# def delete_spare_part(request, spare_part_id):
#     spare_part = get_object_or_404(SparePart, id=spare_part_id)

#     if request.method == 'POST':
#         spare_part.delete()
#         return redirect('spare_part_list')  # Redirect to spare part list view






# Technician Views

def technician_list(request):
    technicians = Technician.objects.all()
    return render(request, 'technician/list.html', {'technicians': technicians})

def create_technician(request):
    if request.method == 'POST':
        form = TechnicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('technician_list')  # Redirect to technician list view

    else:
        form = TechnicianForm()

    return render(request, 'technician/create.html', {'form': form})

def update_technician(request, technician_id):
    technician = get_object_or_404(Technician, id=technician_id)

    if request.method == 'POST':
        form = TechnicianForm(request.POST, instance=technician)
        if form.is_valid():
            form.save()
            return redirect('technician_list')  # Redirect to technician list view

    else:
        form = TechnicianForm(instance=technician)

    return render(request, 'technician/update.html', {'form': form, 'technician': technician})

def delete_technician(request, technician_id):
    technician = get_object_or_404(Technician, id=technician_id)

    if request.method == 'POST':
        technician.delete()
        return redirect('technician_list')  # Redirect to technician list view





# # WorkOrder views

# def work_order_list(request):
#     work_orders = WorkOrder.objects.all()
#     return render(request, 'work_order/list.html', {'work_orders': work_orders})

# def create_work_order(request):
#     if request.method == 'POST':
#         form = WorkOrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('work_order_list')  # Redirect to work order list view

#     else:
#         form = WorkOrderForm()

#     return render(request, 'work_order/create.html', {'form': form})

# def update_work_order(request, work_order_id):
#     work_order = get_object_or_404(WorkOrder, id=work_order_id)

#     if request.method == 'POST':
#         form = WorkOrderForm(request.POST, instance=work_order)
#         if form.is_valid():
#             form.save()
#             return redirect('work_order_list')  # Redirect to work order list view

#     else:
#         form = WorkOrderForm(instance=work_order)

#     return render(request, 'work_order/update.html', {'form': form, 'work_order': work_order})

# def delete_work_order(request, work_order_id):
#     work_order = get_object_or_404(WorkOrder, id=work_order_id)

#     if request.method == 'POST':
#         work_order.delete()
#         return redirect('work_order_list')  # Redirect to work order list view







# Assets views
def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'asset/list.html', {'assets': assets})

def create_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')  # Redirect to asset list view

    else:
        form = AssetForm()

    return render(request, 'asset/create.html', {'form': form})

def update_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_list')  # Redirect to asset list view

    else:
        form = AssetForm(instance=asset)

    return render(request, 'asset/update.html', {'form': form, 'asset': asset})

def delete_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')  # Redirect to asset list view
