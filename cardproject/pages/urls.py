from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . views import *
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='pages-home'),
    path('inventory/', views.list_all_cards, name='pages-inventory'),
    path('addcard/', views.add_card, name='add_card'),
    path('stats/', views.stats, name='pages-stats'),
    path('link/', views.link, name='pages-link'),
    path('ebaytracker', views.ebaytracker, name='pages-ebaytracker'),
    path('sellwax/', views.sellwax, name='pages-sellwax'),
    path('delete/<int:card_id>', views.delete_card),
]
