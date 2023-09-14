from django.shortcuts import render, redirect
from .models import EmployeeData
from .forms import EmployeeDataForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from  django.contrib.auth.decorators import login_required

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

def user_login(request):
    #Checking form method is post,then insert data
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        valid_user = authenticate(username=username, password=password)

        if valid_user is not None:
            login(request, valid_user)
            return redirect('dashboard-index')
        
        else:
            context = { 'error': "User Name or Password is incorrect." }
            return render(request, 'authentication/login.html', context)

    return render(request, 'authentication/login.html')

@login_required(login_url='login') # protect unauthorised access and direct link entering
def index(request):
    #Retrieved all data from DB
    employee_data = EmployeeData.objects.all()

    #Checking form method is post
    if request.method == 'POST':
        form = EmployeeDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = EmployeeDataForm()

    context = { 
        'data': employee_data,
        'form': form,
        }
    return render(request, 'dashboard/index.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')
    