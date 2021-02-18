from django.contrib import admin
from . models import Card
# Register your models here.

admin.site.register(Card)

class Card(admin.ModelAdmin):

    radio_fields={'grades':admin.VERTICAL}