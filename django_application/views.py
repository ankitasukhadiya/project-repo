from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Car,BuyCar,User
from .forms import CarForm
from django.core.paginator import Paginator
from django.db.models import Q


def home(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html') 

def thankyou(request):
    data = Car.objects.all().values()
    context = {
        'data' : data,
    }
    return render(request,'thankyou.html',context) 
    
def carlist(request):     
    form = CarForm 
    if 'save' in request.POST :
        data = CarForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('django_application:thankyou')
    return render(request , 'carlist.html',{'form':form})   

def findcar(request):     
    data = Car.objects.all()
    searchdata = request.GET.get('search')
    if searchdata is not None: 
        data = data.filter(Q(make__icontains = searchdata) | Q(year__icontains = searchdata)).distinct()           
    paginator = Paginator(data,10) 
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    context = {
        'data' : data
    }
    return render(request,'findcar.html',context)

   
     
    
        



