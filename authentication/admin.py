from django.contrib import admin
from .models import CustomUser  # replace with your custom user model class name

# If you're trying to unregister your custom user model:
try:
    admin.site.unregister(CustomUser)
except admin.sites.NotRegistered:
    pass

# Then you can re-register it as needed
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # define your admin class as needed
    pass

