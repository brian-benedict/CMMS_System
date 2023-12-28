from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
# workOrder
    path("", views.work_order_list, name='work_order_list'),
    path('work_orders/create/', views.create_work_order, name='create_work_order'),
    path('work_orders/update/<int:work_order_id>/', views.update_work_order, name='update_work_order'),
    path('work_orders/delete/<int:work_order_id>/', views.delete_work_order, name='delete_work_order'),

]