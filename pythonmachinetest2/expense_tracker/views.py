from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    return render(request, 'home.html')

def register_page(request):
    return render(request, 'register.html')

def expense_summary_page(request):
    return render(request, 'expense_summary.html')

def users_list_page(request):
    return render(request, 'users_list.html')

def manage_users_page(request):
    return render(request, 'manage_users.html')

# UPDATED ADMIN LOGIN WITH LOGIN FUNCTIONALITY
def admin_login_page(request):
    # If user is already logged in as admin, redirect to dashboard
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('/admin-dashboard/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('/admin-dashboard/')  # This goes to your custom admin page
        else:
            # Show error message
            return render(request, 'admin_login.html', {
                'error': 'Invalid username or password. Please try again.'
            })
    
    return render(request, 'admin_login.html')

def is_staff_user(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff_user)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')