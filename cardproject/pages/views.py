from django.shortcuts import render, redirect
from pages.models import *
from django.http import HttpResponse
from django.urls import path
from pages.forms import CardForm


def home(request):
    return render(request, 'pages/home.html')

def list_all_cards(request):
    all_cards = Card.objects.all()
    
    context= {
        "cards":all_cards,
    }
    return render(request,'pages/inventory.html', context)

def add_card(request):
    if request.method == 'GET':
        context={
        }
        return render(request, 'pages/addcard.html', context)
    
    elif request.method == 'POST':
        total = ("lname","fname","cardco","cardyear","gradco","cardgrade","comp","cost")
        print(request.POST.get(total))
        card_instance = Card(request.POST.get(total))
        card_instance.save()
        return redirect('/')

def stats(request):
    return render(request, 'pages/stats.html')

def ebaytracker(request):
    return render(request, 'pages/ebaytracker.html')

def sellwax(request):
    return render(request, 'pages/sellwax.html')