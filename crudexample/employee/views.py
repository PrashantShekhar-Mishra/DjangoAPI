from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    # def list(self, request):
    #     search = request.GET.get('search')
    #     queryset = self.queryset
    #     if search:
    #         queryset = queryset.filter(ename__startswith=search)  # Corrected filter lookup
    #     serializer = EmployeeSerializer(queryset, many=False)      # Added many=True
    #     return Response(serializer.data, status=status.HTTP_200_OK)
