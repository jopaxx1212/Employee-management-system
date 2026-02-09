from django.contrib import admin
from django.urls import path
from .views import ProjectListCreateAPIView, DepartmentListCreateAPIView, EmployeeListCreateAPIView

urlpatterns = [
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('departments/', DepartmentListCreateAPIView.as_view(), name='department-list-create'),
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
]