from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, Admin, Employee, ServiceUser, Visit
from .serializers import CompanySerializer, AdminSerializer, EmployeeSerializer, ServiceUserSerializer, VisitSerializer
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView

class CompanyCreateView(APIView):
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Update an existing company
class CompanyUpdateView(RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# List all companies
class CompanyListView(ListAPIView):
   def get(self, request, *args, **kwargs):
       queryset = Company.objects.all()
       serializer= CompanySerializer(queryset, many=True)
       return Response({'message': 'success','status':status.HTTP_200_OK, 'data': serializer.data})
   

   #  def get(self, request, *args, **kwargs):
   #    queryset= Department.objects.all()
   #    serializer= DepartmentSerializre(queryset, many=True)
   #    return Response({'message': 'success','status':status.HTTP_200_OK, 'data': serializer.data})
    
   #  serializer_class = CompanySerializer
   # return Response()



# Create a new admin profile
class AdminCreateView(CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

# Update an admin profile
class AdminUpdateView(RetrieveUpdateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

# List all admin profiles
class AdminListView(ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


# Create a new employee profile
class EmployeeCreateView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Update an employee profile
class EmployeeUpdateView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# List employees under a specific admin
class EmployeeListView(ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        admin_id = self.kwargs['admin_id']  # Get admin ID from URL
        return Employee.objects.filter(admin__id=admin_id)  # Filter employees by admin


# Create a new service user profile
class ServiceUserCreateView(CreateAPIView):
    queryset = ServiceUser.objects.all()
    serializer_class = ServiceUserSerializer

# Update a service user profile
class ServiceUserUpdateView(RetrieveUpdateAPIView):
    queryset = ServiceUser.objects.all()
    serializer_class = ServiceUserSerializer

# List service users under a specific admin
class ServiceUserListView(ListAPIView):
    serializer_class = ServiceUserSerializer

    def get_queryset(self):
        admin_id = self.kwargs['admin_id']  # Get admin ID from the URL
        return ServiceUser.objects.filter(admin__id=admin_id)  # Filter service users by admin
    
# Visit management

# Create a new visit
class VisitCreateView(CreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

# Update an existing visit
class VisitUpdateView(RetrieveUpdateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

# List all visits
class VisitListView(ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    
