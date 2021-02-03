from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50)
    card_year = models.IntegerField()
    grading_type = models.CharField(max_length=50)
    graded_score = models.IntegerField()
    current_value = models.IntegerField()
    purchase_price = models.IntegerField()
    photo_url =models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)