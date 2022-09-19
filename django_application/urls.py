from django import views
from django.urls import path
from django.conf import settings
from . import views
app_name = 'django_application'

urlpatterns = [
    path('home/',views.home, name='home'),
    path('base/',views.base, name='base'),
    path('carlist/',views.carlist, name='carlist'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('findcar/',views.findcar, name='findcar'),
]