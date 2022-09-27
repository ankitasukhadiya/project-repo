from pyexpat import model
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator,MinMoneyValidator
from moneyed import USD
from djmoney.money import Money
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils.translation import gettext_lazy as _

condition_choices = (
    ('poor','poor'),
    ('fair','fair'),
    ('good','good'),
    ('excellent','excellent')
)
car_status = (
    ('available','available'),
    ('sold','sold'),
)
class Car(models.Model):
    seller_name = models.CharField(max_length=100)
    seller_mobile = models.CharField(max_length=10)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    year = models.DateField()
    condition = models.CharField(max_length=20, choices=condition_choices)
    asking_price = MoneyField(max_digits=10,decimal_places=2,default_currency='USD',
    validators=[MinMoneyValidator(Money(1000,'USD')),MaxMoneyValidator(Money(100000,'USD'))])
    status = models.CharField(max_length=20,choices = car_status,null=True)
    User = models.ForeignKey('User',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.seller_name

class  BuyCar(models.Model):
    Car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True)   
    buyer_name = models.CharField(max_length=50)
    buyer_number = models.CharField(max_length=10)
    commission = MoneyField(max_digits=10,decimal_places=2,default_currency='USD',default=0)
    net_amount = MoneyField(max_digits=10,decimal_places=2,default_currency='USD',default=0) 
    User = models.ForeignKey('User',on_delete=models.CASCADE,null=True)
        
    def _str_(self):
        return self.buyer_name

    @property
    def commission(self):
        commission = (self.Car.asking_price * 5) /100  
        return commission  

    @property
    def net_amount(self):
        commission = (self.Car.asking_price * 5) /100       
        net_amount = (self.Car.asking_price) - commission 
        return net_amount    

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'),max_length=50,unique=True)
    phone_no = models.CharField(max_length=10)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  []
    objects = UserManager()

# @property
# def commission(self):
#     commission = self.asking_price * 5 /100  
#     return commission 

# @property
# def net_amolunt(self):       
#     net_amount = self.asking_price - commission 
#     return net_amount

# class Images(models.Model):
#     Car = models.ForeignKey('Car',on_delete=models.CASCADE,null=True)
#     BuyCar = models.ForeignKey('BuyCar',on_delete=models.CASCADE,null=True)
#     image = models.ImageField()






