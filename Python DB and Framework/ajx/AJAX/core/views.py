from django.shortcuts import render
from django.http import JsonResponse
from .models import Professional

def index(request):
    return render(request, "index.html")

# ADD
def add(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    speciality = request.GET.get('speciality')
    contact = request.GET.get('contact')

    Professional.objects.create(
        username=username,
        email=email,
        speciality=speciality,
        contact_number=contact
    )

    return JsonResponse({"msg": "Added Successfully"})

# DISPLAY
def show(request):
    data = Professional.objects.all()
    return JsonResponse({"data": list(data.values())})

from django.shortcuts import render
from django.http import JsonResponse
from .models import Professional

def index(request):
    return render(request, "index.html")

# ADD
def add(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    speciality = request.GET.get('speciality')
    contact = request.GET.get('contact')

    Professional.objects.create(
        username=username,
        email=email,
        speciality=speciality,
        contact_number=contact
    )

    return JsonResponse({"msg": "Added Successfully"})

# SHOW
def show(request):
    data = Professional.objects.all()
    return JsonResponse({"data": list(data.values())})

# DELETE
def delete(request):
    id = request.GET.get('id')
    Professional.objects.filter(id=id).delete()
    return JsonResponse({"msg": "Deleted Successfully"})

# GET SINGLE (for edit)
def get_one(request):
    id = request.GET.get('id')
    data = Professional.objects.filter(id=id)
    return JsonResponse({"data": list(data.values())})

# UPDATE
def update(request):
    id = request.GET.get('id')
    username = request.GET.get('username')
    email = request.GET.get('email')
    speciality = request.GET.get('speciality')
    contact = request.GET.get('contact')

    obj = Professional.objects.get(id=id)
    obj.username = username
    obj.email = email
    obj.speciality = speciality
    obj.contact_number = contact
    obj.save()

    return JsonResponse({"msg": "Updated Successfully"})