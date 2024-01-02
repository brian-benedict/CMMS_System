from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    # Login view
    # path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Logout view
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),    

# User registration
    # path('register/', views.register, name='register'),

# Report
    path('generate_report/<int:report_id>/', views.generate_report, name='generate_report'),


# Asset
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/create/', views.create_asset, name='create_asset'),
    path('assets/update/<int:asset_id>/', views.update_asset, name='update_asset'),
    path('assets/delete/<int:asset_id>/', views.delete_asset, name='delete_asset'),



# Technician
    path('technicians/', views.technician_list, name='technician_list'),
    path('technicians/create/', views.create_technician, name='create_technician'),
    path('technicians/update/<int:technician_id>/', views.update_technician, name='update_technician'),
    path('technicians/delete/<int:technician_id>/', views.delete_technician, name='delete_technician'), 


# # Spareparts
#     path('spare_parts/', views.spare_part_list, name='spare_part_list'),
#     path('spare_parts/create/', views.create_spare_part, name='create_spare_part'),
#     path('spare_parts/update/<int:spare_part_id>/', views.update_spare_part, name='update_spare_part'),
#     path('spare_parts/delete/<int:spare_part_id>/', views.delete_spare_part, name='delete_spare_part'),

# Maintenanc task
    path('maintenance-tasks/', views.maintenance_task_list, name='maintenance_task_list'),
    path('maintenance-tasks/create/', views.create_maintenance_task, name='create_maintenance_task'),
    path('maintenance-tasks/update/<int:task_id>/', views.update_maintenance_task, name='update_maintenance_task'),
    path('maintenance-tasks/delete/<int:task_id>/', views.delete_maintenance_task, name='delete_maintenance_task'),

]




