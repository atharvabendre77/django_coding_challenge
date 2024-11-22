from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Organization, CustomUser, Role
from .forms import OrganizationForm, CustomUserForm, RoleAssignmentForm

@login_required
def organization_list(request):
    if request.user.is_superuser:
        organizations = Organization.objects.all()
    else:
        organizations = Organization.objects.filter(id=request.user.organization.id)
    return render(request, 'organization_list.html', {'organizations': organizations})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def organization_create(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organization_list')
    else:
        form = OrganizationForm()
    return render(request, 'organization_form.html', {'form': form})

@login_required
def user_management(request):
    users = CustomUser.objects.filter(organization=request.user.organization)
    return render(request, 'user_management.html', {'users': users})

@login_required
def role_assignment(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id, organization=request.user.organization)
    if request.method == 'POST':
        form = RoleAssignmentForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_management')
    else:
        form = RoleAssignmentForm(instance=user)
    return render(request, 'role_assignment_form.html', {'form': form, 'user': user})
