from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Asset Management
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/<int:asset_id>/', views.asset_detail, name='asset_detail'),

    # Maintenance Tasks
    path('maintenance-tasks/', views.maintenance_task_list, name='maintenance_task_list'),
    path('maintenance-tasks/<int:task_id>/', views.maintenance_task_detail, name='maintenance_task_detail'),

    # Work Orders
    path('work-orders/', views.work_order_list, name='work_order_list'),
    path('work-orders/<int:order_id>/', views.work_order_detail, name='work_order_detail'),

    # Maintenance History
    path('maintenance-history/', views.maintenance_history_list, name='maintenance_history_list'),
    path('maintenance-history/<int:history_id>/', views.maintenance_history_detail, name='maintenance_history_detail'),

    # Spare Parts
    path('spare-parts/', views.spare_part_list, name='spare_part_list'),
    path('spare-parts/<int:part_id>/', views.spare_part_detail, name='spare_part_detail'),

    # Reporting
    path('reports/', views.report_list, name='report_list'),
    path('reports/<int:report_id>/', views.report_detail, name='report_detail'),


]
