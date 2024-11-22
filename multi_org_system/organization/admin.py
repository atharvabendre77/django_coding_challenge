from django.contrib import admin
from .models import Organization, Role, CustomUser

admin.site.register(Organization)
admin.site.register(Role)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'organization', 'role']
    list_filter = ['organization', 'role']
