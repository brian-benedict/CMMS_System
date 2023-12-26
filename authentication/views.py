from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})






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


