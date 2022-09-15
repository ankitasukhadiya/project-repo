from pyexpat import model
from tkinter import CASCADE
from wsgiref.validate import validator
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator,MinMoneyValidator
from moneyed import USD

condition_choices = (
    ('poor','poor'),
    ('fair','fair'),
    ('good','good'),
    ('excellent','excellent')
)
class Car(models.Model):
    seller_name = models.CharField(max_length=100)
    seller_mobile = models.CharField(max_length=10)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.DateField()
    condition = models.CharField(max_length=20, choices=condition_choices)
    asking_price = MoneyField(max_digits=10,decimal_places=2,default_currency='USD',validators=[MinMoneyValidator(1000),MaxMoneyValidator(100000)])
  
    def __str__(self):
        return self.seller_name

# class  BuyCar(models.Model):
#     Car = models.ForeignKey(Car,on_delete=models.CASCADE)   
#     buyer_name = models.CharField(max_length=50)
#     buyer_number = models.CharField(max_length=10)
#     price = models.IntegerField(max_length=20)
#     interestedparty_name = models.CharField(max_length=20)
#     commission = models.FloatField(max_length=20)
#     net_amount = models.CharField(max_length=50)

#     def _str_(self):
#         return self.buyer_name

