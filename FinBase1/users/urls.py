from django.urls import path
from . import views

app_name = 'unique_admin_namespace'

urlpatterns = [
    path('create_user/', views.UserCreate.as_view(), name='create-user'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/profile/', views.UserProfileRetrieveUpdate.as_view(), name='user-profile'),
    path('users/change_password', views.ChangePasswordView.as_view(), name='change-password'),
]
