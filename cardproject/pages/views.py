from django.shortcuts import render
from django.http import HttpResponse

def home(reqest):
    return render(request, 'pages/home.html')

def inventory(request):
    return render(request, 'pages/inventory.html')

def stats(request):
    return render(request, 'pages/stats.html')

def ebaytracker(request):
    return render(request, 'pages/ebaytracker.html')

def sellwax(request):
    return render(request, 'pages/sellwax.html')