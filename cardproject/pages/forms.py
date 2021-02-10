from django import forms 
from pages.models import Card 

class CardForm(forms.ModelForm):
    
    class Meta:
        model = Card
        fields = ['first_name','last_name','card_type','card_year','grading_type','graded_score','market_value','purchase_fees']