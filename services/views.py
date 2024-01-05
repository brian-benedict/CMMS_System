from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServiceRequestForm
from .models import ServiceRequest
from inventory.models import SparePart
from django.contrib.auth.decorators import login_required, user_passes_test

def user_view(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.requester = request.user
            service_request.save()
            return redirect('user_view')
    else:
        form = ServiceRequestForm()

    service_requests = ServiceRequest.objects.filter(requester=request.user)
    return render(request, 'services/user_view.html', {'form': form, 'service_requests': service_requests})

def superuser_view(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'services/superuser_view.html', {'service_requests': service_requests})






@login_required
@user_passes_test(lambda u: u.is_superuser)
def update_engineer_feed(request, request_id):
    if request.method == 'POST':
        service_request = get_object_or_404(ServiceRequest, id=request_id)
        new_status = request.POST.get('engineer_feed')
        if new_status in [choice[0] for choice in ServiceRequest.STATUS_CHOICES]:
            service_request.engineer_feed = new_status
            service_request.save()
    return redirect('superuser_view')




@login_required
def update_user_feed(request, request_id):
    if request.method == 'POST':
        service_request = get_object_or_404(ServiceRequest, id=request_id, requester=request.user)
        service_request.user_feed = not service_request.user_feed
        service_request.save()
    return redirect('user_view')





# In views.py

from django.http import JsonResponse
from .models import ServiceRequest, ServiceRequestSparePart

def search_spare_parts(request):
    query = request.GET.get('q', '')
    spare_parts = list(SparePart.objects.filter(part_name__icontains=query).values('id', 'part_name', 'quantity_on_hand'))
    return JsonResponse(spare_parts, safe=False)

def add_spare_part_to_request(request, request_id):
    if request.method == 'POST':
        spare_part_id = request.POST.get('spare_part_id')
        quantity = request.POST.get('quantity')
        spare_part = SparePart.objects.get(id=spare_part_id)
        service_request = ServiceRequest.objects.get(id=request_id)

        # Create or update the demand
        obj, created = ServiceRequestSparePart.objects.update_or_create(
            service_request=service_request, spare_part=spare_part,
            defaults={'quantity_demanded': quantity}
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
