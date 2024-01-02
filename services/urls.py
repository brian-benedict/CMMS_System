from django.urls import path
from . import views

urlpatterns = [
    # URL for normal users to view and submit service requests
    path('user-requests/', views.user_view, name='user_view'),
    # path('user-requests/', views.user_view, name='user_view'),


    # URL for superusers to view all service requests and update engineer feed
    path('superuser-requests/', views.superuser_view, name='superuser_view'),

    # URL for updating the engineer feed (status of the service request)
    path('update-engineer-feed/<int:request_id>/', views.update_engineer_feed, name='update_engineer_feed'),

    # URL for users to update their feed (marking a request as done)
    path('update-user-feed/<int:request_id>/', views.update_user_feed, name='update_user_feed'),
]

