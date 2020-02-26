from django.shortcuts import render

def index(request):
	return render(request,"hrapp/index.html")

def about(request):
	return render(request,"hrapp/about.html")	

