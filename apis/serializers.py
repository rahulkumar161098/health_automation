from rest_framework import serializers
from .models import Company, Admin, Employee, ServiceUser, Visit

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'website']
    
    # Additional validation
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Company name cannot be empty.")
        return value


class AdminSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True) 

    class Meta:
        model = Admin
        fields = ['id', 'company', 'name', 'email', 'phone_number']
    
    def validate_email(self, value):
        if not value.strip():
            raise serializers.ValidationError("Email cannot be empty.")
        return value

    def validate_phone_number(self, value):
        if not value.strip():
            raise serializers.ValidationError("Phone number cannot be empty.")
        return value
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'admin', 'name', 'email', 'phone_number']
    
    def validate_email(self, value):
        if not value.strip():
            raise serializers.ValidationError("Email cannot be empty.")
        return value

    def validate_phone_number(self, value):
        if not value.strip():
            raise serializers.ValidationError("Phone number cannot be empty.")
        return value
    
class ServiceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceUser
        fields = ['id', 'admin', 'name', 'email', 'phone_number']
    
    def validate_email(self, value):
        if not value.strip():
            raise serializers.ValidationError("Email cannot be empty.")
        return value

    def validate_phone_number(self, value):
        if not value.strip():
            raise serializers.ValidationError("Phone number cannot be empty.")
        return value
    
class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'company', 'admin', 'employee', 'service_user', 'assigned_date', 'assigned_starttime', 'assigned_endtime', 'status', 'distance']
    
    def validate(self, data):
        # Validate that the start time is before the end time
        if data['assigned_starttime'] >= data['assigned_endtime']:
            raise serializers.ValidationError("Assigned start time must be before the assigned end time.")
        return data