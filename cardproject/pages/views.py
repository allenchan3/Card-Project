from django.shortcuts import render, redirect
from pages.models import *
from django.http import HttpResponse
from django.urls import path


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
        last_name = (request.POST.get("last_name"))
        first_name = (request.POST.get("first_name"))
        card_type = (request.POST.get("card_type"))
        card_year = (request.POST.get("card_year"))
        grading_type = (request.POST.get("grading_type"))
        graded_score = (request.POST.get("graded_score"))
        market_value = (request.POST.get("market_value"))
        purchase_fees = (request.POST.get("purchase_fees"))
        new_card_instance = Card( last_name=last_name,first_name=first_name, card_type=card_type, card_year=card_year, grading_type=grading_type, graded_score=graded_score, market_value=market_value, purchase_fees=purchase_fees )
        new_card_instance.save()
        return redirect('/')


def stats(request):
    return render(request, 'pages/stats.html')

def ebaytracker(request):
    return render(request, 'pages/ebaytracker.html')

def sellwax(request):
    return render(request, 'pages/sellwax.html')