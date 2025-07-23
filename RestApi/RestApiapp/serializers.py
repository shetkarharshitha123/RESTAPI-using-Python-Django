# from .models import Employee
# from rest_framework import serializers

# class EmployeeSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = '__all__'
#         # fields = ['ename','eid','etreatment']
#         # exclude=['eid']




from rest_framework import serializers
from .models import Employee

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
