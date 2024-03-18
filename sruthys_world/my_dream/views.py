from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_dream(request):
    return render(request,"my_dream.html")

def newborn(request):
    return render(request, "newborn.html")

def accessories(request):
    return render(request, "accessories.html")

def diaper(request):
    return render(request, "diaper.html")

def lactos(request):
    return render(request, "lactos.html")

def toys(request):
    return render(request, "toys.html")

