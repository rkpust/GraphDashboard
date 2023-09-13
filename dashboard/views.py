from django.shortcuts import render, redirect
from .models import EmployeeData
from .forms import EmployeeDataForm
from django.contrib.auth.models import User

# Create your views here.

def registration(request):
    # user_info = User.objects.all()

    # #Checking form method is post
    # if request.method == 'POST':
    #     reg_form = UserForm(request.POST)
    #     if reg_form.is_valid():
    #         reg_form.save()
    #         return redirect('login')
    # else:
    #     reg_form = UserForm()

    # context = { 
    #     'data': user_info,
    #     'registration_form': reg_form,
    #     }
    return render(request, 'authentication/registration.html')

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
