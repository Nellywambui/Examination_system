from django.shortcuts import render, redirect
from OnlineSystem.forms import StudentForm, StudentComplains, StudentForm1
from OnlineSystem.forms import RegisterForm
from OnlineSystem.forms import RegistrationForm
from django.contrib import messages


# Create your views here.
def index(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form = RegistrationForm()
            messages.success(request, 'User registered successfully!')
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'index.html', {'form': form})


def login(request):
    form = StudentForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    form = StudentComplains()

    return render(request, 'logout.html', {'form': form})


def application(request):
    form = StudentForm1()
    return render(request, 'application.html', {'form': form})


