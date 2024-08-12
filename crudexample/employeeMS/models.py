from django.db import models
from django.core.exceptions import ValidationError

class Departement(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)

class Employeems(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    height = models.FloatField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Departement,null=True,blank=True,on_delete=models.CASCADE,related_name="empoyeems")


    def __str__(self):
        return str(self.id)
