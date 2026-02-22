from rest_framework import serializers
from .models import Certificate, Department, Employee




          
class  DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Certificate
        fields = '__all__'



class EmployeeSerializer(serializers.ModelSerializer):

    #field to accept list of certificate Id
    certificate = serializers.PrimaryKeyRelatedField(
        queryset = Certificate.objects.all(), many=True
    )

    certificate_details = CertificateSerializer(source='certificate',many=True,read_only=True)
    #create a field to accept id of department
    department = serializers.PrimaryKeyRelatedField(queryset = Department.objects.all())

    #to get the department details
    department_details = DepartmentSerializer(source='department',read_only=True)

    #create fields in serializer
    username = serializers.CharField(source='user.username',read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)

    #Field level   -----> Serializer.py
    #validate_fieldname
    def validate_contact(self,value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact must contain only digit")
        if len(value)!=10:
            raise serializers.ValidationError("Contact must be exactly 10 digit")
        
        return value

    class Meta:
        model = Employee
        fields = '__all__'


