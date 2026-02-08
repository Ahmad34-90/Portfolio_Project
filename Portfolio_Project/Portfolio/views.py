from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from .models import Profile, Skills, Experience, Projects, Contact
# Create your views here.

def home(request):
    profile = Profile.objects.first()
    return render(request, "Portfolio/home.html", {"profile":profile})

def about(request):
    profile = Profile.objects.first()
    skills = Skills.objects.all()
    experience = Experience.objects.all()
    return render(request, "Portfolio/about.html",{"profile":profile, "skills":skills, "experience":experience})

def projects(request):
    projects = Projects.objects.all()
    return render(request, "Portfolio/projects.html", {"projects":projects})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"Name: {name}\nEmail: {email}\n\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return render(request, 'Portfolio/contact.html', {
            'success': True
        })

    return render(request, 'Portfolio/contact.html')
