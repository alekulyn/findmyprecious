from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    formfield_overrides={
        map_fields.AddressField:{
            'widgets':map_widgets.GoogleMapsAddressWidget},
    }
