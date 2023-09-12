from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    month = models.CharField(max_length=15)
    attendance = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Employee Attendance'

    def __str__(self):
        return f'{self.month}-{self.attendance}'
