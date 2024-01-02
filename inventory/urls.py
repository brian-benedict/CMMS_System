from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [

# Spareparts
    path("", views.spare_parts_list, name='spare_parts_list'),
    path('spare-parts/create/', views.spare_part_create, name='spare_part_create'),
    path('spare-parts/<int:pk>/update/', views.spare_part_update, name='spare_part_update'),
    path('spare-parts/<int:pk>/delete/', views.spare_part_delete, name='spare_part_delete'),
]