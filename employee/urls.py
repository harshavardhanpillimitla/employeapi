from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import LoadEmployeeDetails

router = routers.DefaultRouter()
router.register('api',LoadEmployeeDetails,'employee')

urlpatterns = router.urls