from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    
    GRADES=(
    ('0','None'),
    ('1','1'),
    ('1.5','1.5'),  
    ('2','2'),
    ('2.5','2.5'),
    ('3','3'),  
    ('3.5','3.5'),
    ('4','4'),
    ('4.5','4.5'),  
    ('5','5'),
    ('5.5','5.5'),
    ('6','6'),    
    ('6.5','6.5'),
    ('7','7'),  
    ('7.5','7.5'),
    ('8','8'),
    ('8.5','8.5'),  
    ('9','9'),
    ('9.5','9.5'),
    ('10','10')  
    )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50)
    card_year = models.IntegerField()
    grading_type = models.CharField(max_length=50,blank=True)
    graded_score = models.CharField(max_length=3,blank=True, choices=GRADES)
    market_value = models.DecimalField(max_digits=7, decimal_places=2) # $99999.99
    purchase_fees = models.DecimalField(max_digits=7, decimal_places=2) # $99999.99
    sell_price = models.DecimalField(max_digits=7, decimal_places=2) # $99999.99
    trend = models.CharField(max_length=5)
    card_photo = models.URLField(max_length=200, null=True, default=None, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.first_name
    
    #creates a structure that is applied to the database, not class but after applying migrations
    
    #python manage.py makemigrations
    #python manage.py migrate