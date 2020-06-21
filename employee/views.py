from django.shortcuts import render

from .models import Employee,ActivityPeriods
from rest_framework import viewsets,permissions


from .serializer import EmployeeDetailSerializer

class LoadEmployeeDetails(viewsets.ModelViewSet):
    serializer_class = EmployeeDetailSerializer

    def get_queryset(self):
        return Employee.objects.all()
