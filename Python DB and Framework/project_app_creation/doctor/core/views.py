from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def home(request):
    doctors = Doctor.objects.all()
    return render(request, "home.html", {"doctors": doctors})

def profile(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    return render(request, "profile.html", {"doctor": doctor})


def contact(request):
    return render(request, "contact.html")


def update_doctor(request, id):
    doctor = Doctor.objects.get(id=id)

    if request.method == "POST":
        doctor.name = request.POST.get("name")
        doctor.specialization = request.POST.get("specialization")
        doctor.experience = request.POST.get("experience")
        doctor.city = request.POST.get("city")
        doctor.save()

        return redirect("home")

    return render(request, "update.html", {"doctor": doctor})

def delete_doctor(request, id):
    Doctor.objects.get(id=id).delete()
    return redirect("home")