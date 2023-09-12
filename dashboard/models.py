from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    month = models.CharField(max_length=15)
    attendace = models.IntegerField()

    def __str__(self):
        return f'{self.month}-{self.attendace}'
