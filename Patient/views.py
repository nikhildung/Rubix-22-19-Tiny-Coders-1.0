from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
def Home(request):
    return render(request,'Patient/Index.html')

