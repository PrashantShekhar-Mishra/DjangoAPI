from rest_framework import serializers
from .models import Employeems,Departement

class DepratmentSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Departement
        fields = ['name']

class EmployeemsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Employeems
        fields = '__all__'
        depth=1

    def validate_height(self , value ):
        if value < 5.0 :
            raise serializers.ValidationError("Hight should be greater than 5")
        return value

