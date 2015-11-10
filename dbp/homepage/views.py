from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homepage(request):
	return render(request,'index.html')

def login(request):
	return render(request,'login.html')

def registration(request):
	return render(request, 'registration.html')