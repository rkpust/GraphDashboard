from django.shortcuts import render,HttpResponse
from .models import EmployeeData

# Create your views here.

def index(request):
    employee_data = EmployeeData.objects.all()
    context = { 'data': employee_data, }
    return render(request, 'dashboard/index.html', context)
