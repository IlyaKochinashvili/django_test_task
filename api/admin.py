from django.contrib import admin

# Register your models here.
from api.models import Client, Address


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    exclude = ('zodiac_sing',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
