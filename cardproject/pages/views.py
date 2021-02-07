from django.shortcuts import render
from pages.models import *
from django.http import HttpResponse


def home(request):
    return render(request, 'pages/home.html')

def list_all_cards(request):
    
    all_cards = Card.objects.all()
    print(all_cards)    
    
    context= {
        "cards":all_cards,
    }
    return render(request,'pages/inventory.html', context)

def add_card(request):
    addcard = "<h1> Add Card </h1>"
    return render(request, 'pages/addcard.html')

def stats(request):
    return render(request, 'pages/stats.html')

def ebaytracker(request):
    return render(request, 'pages/ebaytracker.html')

def sellwax(request):
    return render(request, 'pages/sellwax.html')