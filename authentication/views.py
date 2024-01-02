from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login page after registration
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

from django.core.mail import send_mail
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data.get('is_superuser'):
                user.is_active = False  # Do not activate superuser account immediately
                # Send email to existing superusers for confirmation
                superusers = CustomUser.objects.filter(is_superuser=True)
                for superuser in superusers:
                    send_mail(
                        'New Superuser Registration',
                        'A new superuser has requested registration. Please confirm.',
                        'from@example.com',
                        [superuser.email],
                        fail_silently=False,
                    )
            user.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})






from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CustomUser
from django.shortcuts import render, redirect

@login_required
@user_passes_test(lambda u: u.is_superuser)
def superuser_confirmation(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        user = CustomUser.objects.get(id=user_id)

        if action == 'approve':
            user.is_superuser = True
            user.is_superuser_confirmed = True
            user.is_active = True
            user.save()
        elif action == 'deny':
            user.is_superuser_requested = False
            user.save()

    users = CustomUser.objects.filter(is_superuser_requested=True, is_superuser_confirmed=False)
    return render(request, 'superuser_confirmation.html', {'users': users})






def custom_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # print("brian")
            return redirect('dashboard')  # Redirect to the home page or another appropriate page
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'authentication/login.html', {})



def custom_logout(request):
    logout(request)
    return redirect('login')


