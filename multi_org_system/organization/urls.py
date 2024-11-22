from django.urls import path
from . import views

urlpatterns = [
    path('organizations/', views.organization_list, name='organization_list'),
    path('organizations/create/', views.organization_create, name='organization_create'),
    path('users/', views.user_management, name='user_management'),
    path('users/<int:user_id>/assign-role/', views.role_assignment, name='role_assignment'),
]
