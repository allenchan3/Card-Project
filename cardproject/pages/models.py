from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50)
    card_year = models.IntegerField()
    grading_type = models.CharField(max_length=50)
    graded_score = models.IntegerField()
    market_value = models.DecimalField(max_digits=7, decimal_places=2) # $99999.99
    purchase_fees = models.DecimalField(max_digits=7, decimal_places=2) # $99999.99
    trend = models.CharField(max_length=5)
    card_photo = models.URLField(max_length=200, null=True, default= None, blank =True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)