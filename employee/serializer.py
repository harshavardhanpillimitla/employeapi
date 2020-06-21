from rest_framework import serializers
from .models import Employee,ActivityPeriods




class ActivityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = ['Start_Time',
                'End_Time'
        
        ]




class EmployeeDetailSerializer(serializers.ModelSerializer):
    activity_periods = ActivityDetailSerializer(many=True)
    class Meta:
        model = Employee
        fields = [
            'employeeId',
            'employeeName',
            'timeZone',
            'activity_periods'
        ]

    
