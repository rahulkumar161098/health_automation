# Generated by Django 5.1.1 on 2024-09-11 09:16

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_serviceuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateField(default=django.utils.timezone.now)),
                ('assigned_starttime', models.TimeField()),
                ('assigned_endtime', models.TimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=50)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='apis.admin')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='apis.company')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='apis.employee')),
                ('service_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='apis.serviceuser')),
            ],
        ),
    ]
