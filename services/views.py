from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServiceRequestForm
from .models import ServiceRequest
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

