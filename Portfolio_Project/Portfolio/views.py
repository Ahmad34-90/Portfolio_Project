from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "Portfolio/home.html")

def about(request):
    return render(request, "Portfolio/about.html")

def projects(request):
    return render(request, "Portfolio/projects.html")

def contact(request):
    return render(request, "Portfolio/contact.html")