from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register-page/', views.register_page, name='register-page'),
    path('expense-summary-page/', views.expense_summary_page, name='expense-summary-page'),
    path('users-list/', views.users_list_page, name='users-list-page'),
    path('admin-manage-users/', views.manage_users_page, name='manage-users-page'),
    path('admin-login/', views.admin_login_page, name='admin-login'),  # This line must exist
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),
    path('users/', include('users.urls')),
    path('expenses/', include('expenses.urls')),
]