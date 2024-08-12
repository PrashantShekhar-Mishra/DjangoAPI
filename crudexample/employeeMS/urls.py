from django.urls import path,include
from .views import EmployeeMSView

urlpatterns = [
    path('emloyeems/',EmployeeMSView.as_view(),name="employee_ms_view"),
    path('emloyeems/<int:pk>',EmployeeMSView.as_view(),name="employee_ms_view_pk")
]
