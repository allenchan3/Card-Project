from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'pages/home.html')

def list_all_cards(request):
    return HttpResponse('<h1>Test </h1>')

def stats(request):
    return render(request, 'pages/stats.html')

def ebaytracker(request):
    return render(request, 'pages/ebaytracker.html')

def sellwax(request):
    return render(request, 'pages/sellwax.html')