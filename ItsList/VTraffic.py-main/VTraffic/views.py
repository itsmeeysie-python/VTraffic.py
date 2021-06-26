from django.shortcuts import render, redirect

def VT(request):
	return render(request, 'VTform.html')