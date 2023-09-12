from django import forms
from .models import EmployeeData

class EmployeeDataForm(forms.ModelForm):
    class Meta:
        model = EmployeeData
        fields = '__all__'
