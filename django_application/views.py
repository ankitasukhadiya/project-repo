from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Car
from .forms import CarForm


def home(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html') 

def thankyou(request):
    return render(request,'thankyou.html') 
    
def carlist(request):
    # return render(request,'carlist.html') 
    form = CarForm 
    if 'save' in request.POST :
        data = CarForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            return redirect('django_application:thankyou')
    return render(request , 'carlist.html',{'form':form})        




