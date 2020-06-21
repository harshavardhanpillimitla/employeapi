from django.db import models

class Employee(models.Model):
    employeeId = models.CharField(max_length=10)
    employeeName = models.CharField(max_length=30)
    timeZone = models.CharField(max_length=30)




class ActivityPeriods(models.Model):
    EmployeeRef = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='activity_periods')
    Start_Time = models.DateTimeField() 
    End_Time = models.DateTimeField() 