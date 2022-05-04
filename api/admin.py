from django.contrib import admin
from api.models import Gestion, Sale, Support, Client, Contract, Event


@admin.register(Gestion)
class GestionAdmin(admin.ModelAdmin):
    #list_display = ()
    pass


@admin.register(Sale)
class SalesAdmin(admin.ModelAdmin):
    #list_display = ()
    pass


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    #list_display = ()
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company_name')

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'status')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('client', 'attendees', 'status')
