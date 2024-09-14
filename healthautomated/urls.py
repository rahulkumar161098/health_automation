
from django.contrib import admin
from django.urls import path
from apis.views import CompanyCreateView, CompanyUpdateView, CompanyListView, AdminCreateView, AdminUpdateView, AdminListView, EmployeeCreateView, EmployeeUpdateView, EmployeeListView, ServiceUserCreateView, ServiceUserUpdateView, ServiceUserListView, VisitCreateView, VisitUpdateView, VisitListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/create/', CompanyCreateView.as_view(), name='create-company'),
    path('company/update/<int:pk>/', CompanyUpdateView.as_view(), name='update-company'),
    path('company/list/', CompanyListView.as_view(), name='list-companies'),  

    # Admin Management
    path('c_admin/create/', AdminCreateView.as_view(), name='create-admin'),
    path('c_admin/update/<int:pk>/', AdminUpdateView.as_view(), name='update-admin'),
    path('c_admin/list/', AdminListView.as_view(), name='list-admins'),

     # Employee Management
    path('employee/create/', EmployeeCreateView.as_view(), name='create-employee'),
    path('employee/update/<int:pk>/', EmployeeUpdateView.as_view(), name='update-employee'),
    path('employee/list/<int:admin_id>/', EmployeeListView.as_view(), name='list-employees'),

     # Service User Management
    path('service-user/create/', ServiceUserCreateView.as_view(), name='create-service-user'),
    path('service-user/update/<int:pk>/', ServiceUserUpdateView.as_view(), name='update-service-user'),
    path('service-user/list/<int:admin_id>/', ServiceUserListView.as_view(), name='list-service-users'),

    # Visit Management
    path('visit/create/', VisitCreateView.as_view(), name='create-visit'),
    path('visit/update/<int:pk>/', VisitUpdateView.as_view(), name='update-visit'),
    path('visit/list/', VisitListView.as_view(), name='list-visits'),
]
