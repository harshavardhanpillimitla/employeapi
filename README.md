# employeapi


we create models with required fields along with relationship like foreignkey 


we declare serializer by import serializer from rest_framework 

and write nested serializer for two models employee and activityperiods



and creating view for the serializer class 


and adding the corresponding urls to the app


it is simple api so we can dumpdata to the api

by using python manage.py dumpdata appname  --format json --indent 2 > employee.json


we load data by using the  ython manage.py   employee.json


