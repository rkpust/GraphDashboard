from django.shortcuts import render, redirect
from .models import EmployeeData
from .forms import EmployeeDataForm

# Create your views here.

def index(request):
    #Retrieved all data from DB
    employee_data = EmployeeData.objects.all()

    #Checking form method is post
    if request.method == 'POST':
        form = EmployeeDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeDataForm()

    context = { 
        'data': employee_data,
        'form': form,
        }
    return render(request, 'dashboard/index.html', context)
