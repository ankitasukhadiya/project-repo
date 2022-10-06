from django.contrib import admin
from django.conf import settings
from .models import Car,User,BuyCar,CarImage
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

admin.site.register(CarImage)
admin.site.register(Car)
admin.site.register(User)
admin.site.register(BuyCar)

class UserAdmin(admin.ModelAdmin):
    formfield_overrides = {map_fields.AddressField:{'widget':map_widgets.GoogleMapsAddressWidget},
    }
