from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
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