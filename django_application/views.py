from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Car
from .forms import CarForm
from django.core.paginator import Paginator


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

def findcar(request):
    return render(request,'findcar.html')
    # data = Car.objects.all()   
    # paginator = Paginator(data, 5) 
    # page_number = request.GET.get('page')
    # data = paginator.get_page(page_number)
    # context = {
    #         'data': data,
    #     }     
    # return render(request, "findcar.html", context)



