from django.contrib import admin
from apis.models import Company, Admin, Employee, Visit

# Register your models here.
admin.site.register(Company)
admin.site.register(Admin)
admin.site.register(Employee)
admin.site.register(Visit)