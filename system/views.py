from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Report
from .models import MaintenanceHistory
from .models import SparePart
from .models import Technician
from .models import WorkOrder
from .models import Asset
from .models import MaintenanceTask





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




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Change to your desired post-registration page

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def generate_report(request, report_id):
    # Get the report based on the report_id
    report = Report.objects.get(id=report_id)
    
    # Perform queries or data processing here to generate the report data
    # You can use Django's QuerySet to retrieve data and process it

    # For example, if you need to retrieve a list of assets, you might use:
    # assets = Asset.objects.filter(some_criteria)

    # Then, pass the report data to the template
    context = {
        'report': report,
        # Include any data needed for your report
        # 'assets': assets,
    }

    return render(request, 'reporting/report.html', context)




def maintenance_history_list(request):
    history_entries = MaintenanceHistory.objects.all()
    return render(request, 'maintenance_history/list.html', {'history_entries': history_entries})




def spare_part_list(request):
    spare_parts = SparePart.objects.all()
    return render(request, 'spare_part/list.html', {'spare_parts': spare_parts})

def create_spare_part(request):
    # Handle spare part creation form submission here
    if request.method == 'POST':
        # Process and save the spare part
        # Redirect to spare part list view

    return render(request, 'spare_part/create.html')

def update_spare_part(request, spare_part_id):
    # Handle spare part update form submission here
    if request.method == 'POST':
        # Process and update the spare part
        # Redirect to spare part list view

    spare_part = SparePart.objects.get(id=spare_part_id)
    return render(request, 'spare_part/update.html', {'spare_part': spare_part})

def delete_spare_part(request, spare_part_id):
    # Handle spare part deletion here
    # Redirect to spare part list view




def technician_list(request):
    technicians = Technician.objects.all()
    return render(request, 'technician/list.html', {'technicians': technicians})

def create_technician(request):
    # Handle technician creation form submission here
    if request.method == 'POST':
        # Process and save the technician
        # Redirect to technician list view

    return render(request, 'technician/create.html')

def update_technician(request, technician_id):
    # Handle technician update form submission here
    if request.method == 'POST':
        # Process and update the technician
        # Redirect to technician list view

    technician = Technician.objects.get(id=technician_id)
    return render(request, 'technician/update.html', {'technician': technician})

def delete_technician(request, technician_id):
    # Handle technician deletion here
    # Redirect to technician list view




def work_order_list(request):
    work_orders = WorkOrder.objects.all()
    return render(request, 'work_order/list.html', {'work_orders': work_orders})

def create_work_order(request):
    # Handle work order creation form submission here
    if request.method == 'POST':
        # Process and save the work order
        # Redirect to work order list view

    return render(request, 'work_order/create.html')

def update_work_order(request, work_order_id):
    # Handle work order update form submission here
    if request.method == 'POST':
        # Process and update the work order
        # Redirect to work order list view

    work_order = WorkOrder.objects.get(id=work_order_id)
    return render(request, 'work_order/update.html', {'work_order': work_order})

def delete_work_order(request, work_order_id):
    # Handle work order deletion here
    # Redirect to work order list view



# views.py
from django.shortcuts import render, redirect
from .models import Asset

def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'asset/list.html', {'assets': assets})

def create_asset(request):
    # Handle asset creation form submission here
    if request.method == 'POST':
        # Process and save the asset
        # Redirect to asset list view

    return render(request, 'asset/create.html')

def update_asset(request, asset_id):
    # Handle asset update form submission here
    if request.method == 'POST':
        # Process and update the asset
        # Redirect to asset list view

    asset = Asset.objects.get(id=asset_id)
    return render(request, 'asset/update.html', {'asset': asset})

def delete_asset(request, asset_id):
    # Handle asset deletion here
    # Redirect to asset list view
