from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def Measurement_optical_equipment(request):
    return render(request,'Measurement_optical_equipment.html')

def Optical_Glasses(request):
    return render(request,'Optical_Glasses.html')

def optical_instruments(request):
    return render(request,'optical_instruments.html')

def crystal(request):
    return render(request,'crystal.html')

def AboutUs(request):
    return render(request,'about_us.html')

def Contact(request):
    return render(request,'Contact.html')