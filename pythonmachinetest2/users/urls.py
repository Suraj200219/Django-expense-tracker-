from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user, name='register'),  # POST /register/
    path('api/', views.UserList.as_view(), name='user-list-api'),  # GET /users/api/
    path('api/<int:pk>/', views.UserDetail.as_view(), name='user-detail-api'),
    path('api/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete-api'),
    path('list/', views.users_list_page, name='users-list-page'),  # GET /users/list/
]