from django.shortcuts import render, redirect
from .models import EmployeeData
from .forms import EmployeeDataForm
from django.contrib.auth.models import User

# Create your views here.

def registration(request):
    #Checking form method is post,then insert data
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        #print(username, email, password, confirm_password) #showed inserted data in terminal

        if password == confirm_password:
            new_user = User.objects.create_user(username, email, password)
            new_user.save()
            return redirect('login')
        else:
            context = { 'error': "Password is not same." }
            return render(request, 'authentication/registration.html', context)

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
