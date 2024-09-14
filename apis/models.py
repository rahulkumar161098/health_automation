from django.db import models
from django.core.validators import URLValidator, EmailValidator, RegexValidator, MinValueValidator
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(validators=[URLValidator], blank=True, null=True)

    def __str__(self):
        return self.name

class Admin(models.Model):
    company = models.ForeignKey(Company, related_name='admins', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator])
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")]
    )

    def __str__(self):
        return f"{self.name} ({self.company.name})"
    
class Employee(models.Model):
    admin = models.ForeignKey(Admin, related_name='employees', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator])
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )

    def __str__(self):
        return f"{self.name} ({self.admin.name})"
    
class ServiceUser(models.Model):
    admin = models.ForeignKey(Admin, related_name='service_users', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator])
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")]
    )

    def __str__(self):
        return f"{self.name} ({self.admin.name})"
    
class Visit(models.Model):
    company = models.ForeignKey(Company, related_name='visits', on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, related_name='visits', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='visits', on_delete=models.CASCADE)
    service_user = models.ForeignKey(ServiceUser, related_name='visits', on_delete=models.CASCADE)
    
    assigned_date = models.DateField(default=timezone.now)
    assigned_starttime = models.TimeField()
    assigned_endtime = models.TimeField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    distance = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"Visit for {self.employee.name} with {self.service_user.name} on {self.assigned_date}"
