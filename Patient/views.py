from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request,'Patient/Html/Index.html')

def Doctor(request):
    return render(request, 'Patient/Html/Doctor_Index.html')

def Doctor_Profile(request):
    return render(request, 'Patient/Html/Doctor_Profile.html')

def Doctor_Pre(request):
    return render(request, 'Patient/Html/Doctor_Precription.html')

def Doctor_Appointment(request):
    return render(request, 'Patient/Html/Appointment.html')

@csrf_exempt
def signup(request):
    ctx = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
        else:

            ctx['form'] = form
    else:
        form = NewUserForm()
        ctx['form'] = form
    return render(request, 'Patient/Html/Signup.html', ctx)


def LOGIN(request):

    if request.POST:
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=pwd)
            print(username,pwd,end='\n')
            if user is not None:
                login(request, user)
                return redirect('Home')

        messages.info(request, 'username and/or password not correct ')

    form = AuthenticationForm()

    return render(request, 'Patient/Html/Login.html', {
        'login_form' : form
    })


def LOGOUT(request):
    logout(request)
    return redirect('Home')