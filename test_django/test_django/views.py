from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = "Hello Django!"
	return render(request,"django.html",context)
	# return HttpResponse("<i style='color:red'>Hello Django!</i>")