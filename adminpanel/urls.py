from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update/<int:report_id>/', views.update_status, name='update_status'),
    path('logout/', views.admin_logout, name='admin_logout'),
]
