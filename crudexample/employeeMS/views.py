from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employeems
from .serializers import EmployeemsSerilizer
from django.shortcuts import get_object_or_404

class EmployeeMSView(APIView):
    def get(self, request, pk=None):
        if pk:
            employeems = get_object_or_404(Employeems, pk=pk)
            serializer = EmployeemsSerilizer(employeems)
            return Response(serializer.data)
        else:
            employeems = Employeems.objects.all()
            serializer = EmployeemsSerilizer(employeems, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = EmployeemsSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        employeems = get_object_or_404(Employeems,pk=pk)
        serializer = EmployeemsSerilizer(employeems,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self , request , pk):
        employeems = get_object_or_404(Employeems,pk=pk)
        serializer = EmployeemsSerilizer(employeems,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employeems = get_object_or_404(Employeems,pk=pk)
        employeems.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        