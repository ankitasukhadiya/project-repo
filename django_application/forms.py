from django import forms
from django.forms import ModelForm
from .models import Car

class DateInput(forms.DateInput):
    input_type =  'date'

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["seller_name","seller_mobile","make","model","year","condition","asking_price"]  
        widgets = {
            'year' : DateInput(),
        }    




