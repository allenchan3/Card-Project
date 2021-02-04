from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pages-home'),
    path('inventory/', views.list_all_cards, name='pages-inventory'),
    path('stats/', views.stats, name='pages-stats'),
    path('ebaytracker', views.ebaytracker, name='pages-ebaytracker'),
    path('sellwax', views.sellwax, name='pages-sellwax'),
]
