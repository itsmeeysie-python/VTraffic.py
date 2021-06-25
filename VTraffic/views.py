from django.shortcuts import redirect, render
from .models import *

def Main(request):
	return render(request, 'main.html')

def Officer(request):

	return render(request, 'officer.html')

def Identification(request):
	return render(request, 'officer.html')

def Officer(request):
	return render(request, 'Identification.html')

def Violators(request):
	return render(request, 'checkout.html')

def Checkout(request):
	return render(request, 'second.html')

def Communicate(request):
	return render(request, 'second.html')

