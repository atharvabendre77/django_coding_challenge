from django import forms
from .models import CustomUser, Organization, Role

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'address', 'is_main']

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'organization', 'role']

class RoleAssignmentForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['role']
