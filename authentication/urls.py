from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # ... other URL patterns ...
    path('register/', views.register, name='register'),
    path('', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='authentication/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'), name='password_reset_complete'),


    # ... other URL patterns ...
]

