from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = ('email',)



class CustomUserCreationForm(UserCreationForm):
    is_superuser = forms.BooleanField(required=False, help_text='Check if registering as a superuser.')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'is_superuser')
